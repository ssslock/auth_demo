'''
Created on 2013-3-27

@author: wuzili
'''
import cherrypy
#import os
#import time
import json
import base64
#import random
import logging

from util import hash as hash_m
#from util import log
from util import network
import config
    
nMax = 8
k = 1


class Root(object):
    def __init__(self):
        self.sessions = []
        self.sn = 0
#        self.stor_connect = network.Connect(config.stor_host, config.stor_port)
        self.stor_connect = network.Connect("192.168.0.4", 7305)
        self.logger = logging.getLogger("server_log")
        
    def __newsession__(self):
        sid = self.sn
        session = {"sid":sid}
        self.sessions.append(session)
        self.sn += 1
        return sid, session
        
    @cherrypy.expose
    def index(self):
        result = 'Running'
        return result

    @cherrypy.expose
    def regcheck(self, username):
        
        return self.stor_connect.request("regcheck", username=username)
        
    @cherrypy.expose
    def reg(self, data):
        serializedRequest = base64.urlsafe_b64decode(str(data))
        print serializedRequest
        request = json.loads(serializedRequest)
        username = request[u"username"]
        authdata = request[u"authdata"]
        n = len(authdata)
        
        return self.stor_connect.request("reg", data=base64.urlsafe_b64encode(json.dumps({u"username": username, u"n":n, u"k":k, u"authdata": authdata})))


    @cherrypy.expose
    def login(self, username):
        data = json.loads(self.stor_connect.request("login", username=username))
        print data
        if data[u"status"] < 0:
            return json.dumps({u"status": -1})
        qData = data[u"qData"]
        n = data[u"n"]
        k = data[u"k"]
        qlist = []
        alist = []
        for partitionArg, hashSalt, keyHash in qData:
            qlist.append((partitionArg, hashSalt))
            alist.append((keyHash))
            
        sid, session = self.__newsession__()
        session[u"data"] = {u"alist":alist, u"k":k, u"n":n}
        
        return json.dumps({u"status": 0, u"sid": sid, u"qlist": qlist})
    
    @cherrypy.expose
    def authA(self, data):
        print data
        serializedRequest = base64.urlsafe_b64decode(str(data))
        request = json.loads(serializedRequest)
        
        sid = request[u"sid"]
        sdata = self.sessions[sid][u"data"]
        alist = sdata[u"alist"]
        alist_ = request[u"alist"]
        n = sdata[u"n"]
        k = sdata[u"k"]
        for i in range(0, n):
            r, keyHash = alist_[i]
            a = alist[i]
            if hash_m.hash(r, a) == keyHash:
                k -= 1
                if k <= 0:
                    return "0"
        return "-1"

def start():
    cherrypy.server.socket_host = config.reg_host
    cherrypy.config.update({'server.socket_port':config.reg_port})
    root = Root()
    cherrypy.quickstart(root)
    
'''
    @cherrypy.expose
    def regnew(self, uname):
        res = json.loads(self.stor_connect.request("regnew", uname=uname, n=n, k=k))
        slist = res["slist"]
        sid, session = self.__newsession__()
        session["data"] = res
        return json.dumps({"sid":sid, "slist":slist})

    @cherrypy.expose
    def regkey(self, sid, hljson):
        kid = self.sessions[sid]["data"]["kid"]
        return self.stor_connect.request("regkey", kid=kid, hljson=hljson)
'''