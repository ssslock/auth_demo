'''
Created on 2013-3-27

@author: wuzili
'''
import cherrypy
#import time
import json
import random
import base64

from util import hash as hash_m
#from util import log
import config
from stor import es

__max_table_len__ = 10

class Root(object):
    def __init__(self, nid):
        self.es = es.ES()
        
        self.tables = {}
        self.nid = nid
        self.tid = nid << 16
        self.kn = 0

    @cherrypy.expose
    def index(self):
        result = 'Running'
        return result

    @cherrypy.expose
    def regcheck(self, username):
        status = -1 if self.es.has_user(username) else 0
        return str(status)
    
    @cherrypy.expose
    def reg(self, data):
        serializedRequest = base64.urlsafe_b64decode(str(data))
        unserializedData = json.loads(serializedRequest)
        status = -1 if self.es.reg(unserializedData) < 0 else 0
        return str(status)

    @cherrypy.expose
    def login(self, username):
        data = self.es.getdatabyusername(username)
        if data is None:
            return json.dumps({u"status":-1})
        authdata = data[u"authdata"]
        n = data[u"n"]
        k = data[u"k"]
        qData = []
        for i in range(0, n):
            partitionArg, hashSalt, keyHash = authdata[i]
            r = random.randint(0, 0x7fffffff)
            qData.append((partitionArg, hash_m.hash(r, hashSalt), hash_m.hash(r, keyHash)))
        print "authdata: "
        print authdata
        print "qData: "
        print qData
        return json.dumps({u"status":0, u"qData":qData, u"k":k, u"n":n})

def start(nid):
    cherrypy.server.socket_host = config.stor_host
    cherrypy.config.update({'server.socket_port':config.stor_port})
    root = Root(nid)
    cherrypy.quickstart(root)
    
    

'''
    @cherrypy.expose
    def regnew(self, uname, n, k):
        n = int(n)
        slist = []
        for i in range(0, n):
            ii = random.randint(0, 0xffff)
            si = random.randint(0, 0xffff)
            slist.append((ii, si))
        kid = self.es.newkey(uname, slist, k)
        if kid < 0:
            return "-1"
        res = {"kid": kid, "slist": slist}
        return json.dumps(res)
    
    @cherrypy.expose
    def regkey(self, kid, hljson):
        hlist = json.loads(hljson)
        if self.es.regkey(kid, hlist):
            return "0"
        return "-1"
'''