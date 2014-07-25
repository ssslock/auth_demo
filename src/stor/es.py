class ES(object):
    def __init__(self):
        self.nid = 0
        self.datas = {}
        self.datas2 = {}
        
    def has_user(self, username):
        return self.datas2.has_key(username)
    
    def reg(self, data):
        username = data[u"username"]
        if self.datas2.has_key(username):
            return -1;
        kid = self.nid;
        data[u"kid"] = kid;
        self.datas[kid] = data
        self.datas2[username] = data
        self.nid = kid + 1;
        return kid

    def getdatabyusername(self, username):
        if self.datas2.has_key(username):
            return self.datas2[username]
        else:
            return None
        
'''   
    def newkey(self, uname, slist, k):
        if self.datas2.has_key(uname):
            return -1
        data = {"uname":uname, "slist":slist, "k":k}
        kid = self.n
        self.n = self.n + 1;
        data["kid"] = kid
        self.datas[kid] = data
        self.datas2[uname] = data
        return kid
    
    def regkey(self, kid, hlist):
        if not self.datas.has_key(kid):
            return False
        self.datas[kid]["hlist"] = hlist
        return True
'''