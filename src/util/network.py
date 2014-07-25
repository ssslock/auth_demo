import urllib2

class Connect(object):
    
    def __init__(self, host, port):
        self.host = host
        self.port = port
    
    def request(self, path, **kwargs):
        url = "http://" + self.host + ":" + str(self.port) +"/" + path
        bFirst = True
        for k, v in kwargs.items():
            url += ('?' if bFirst else '&') + str(k) + '=' + str(v)
            bFirst = False
        print url
        page = urllib2.urlopen(url)
        res = page.read()
        page.close()
        print res
        return res