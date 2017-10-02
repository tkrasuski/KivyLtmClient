import requests as rq
import json as js
import settings as stt

#  comunication class

class Talk:
    def __init__(self):
        self.url = None
        self.user = stt.user
        self.password = stt.password
        self.data= None
        self.session = rq.session()
        self.headers =  {'Content-type': 'application/json', 'Accept': 'text/plain'}
    def post_(self, msg):
        if msg and self.url:
            req = rq.post(self.url, data=js.dumps(self.data), headers=self.headers,verify=False)
            if req.status_code in (200):
                return req.text
            else:
                return req.status_code
        else:
            return None
    def get_(self, msg):
        self.login_()
        req = self.session.get(stt.url+msg, headers=self.headers,verify=False)
        if req.status_code ==200:
            return req.text
        else:
            return 'ERROR:' + req.text
    def put_(self, msg):
        pass
    def login_(self):
        data = dict(login=stt.user, passwd=stt.password)
        req = self.session.post(stt.url+'/serwisy/logmein', data=js.dumps(data), headers=self.headers,verify=False)
        if req.status_code ==200:
            return req.text
        else:
            return 'login error'
        
            
