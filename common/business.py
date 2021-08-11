import requests
import json
from api.config.config import Config
'''
def token(username='developer', password='developer'):
    url = 'http://flash-admin.enilu.cn/prod-api/account/login'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    userdata = {'username': username, 'password': password}

    with requests.post(url=url,
                       headers=headers,
                       data=userdata) as response:
        d = json.loads(response.text)
        return d.get('data').get('token')
'''
class Token:
    """
        获取登录sessionid
        :return:
    """       
    def __init__(self):
        self.__username = Config().testLoginName
        self.__password = Config().testLoginPassword
        self.__url = Config().testLoginUrl
        self.__apitype = Config().testLoginApiType       
        #print(self.__username)
        # self.open()
    def Sessionid(self):
        name =self.__username
        password =self.__password
        url = self.__url
        apitype =self.__apitype
        headers = {
            'Content-Type': apitype
                   }
        userdata = {'username': name, 'password': '12'}
        
        with requests.post(url=url,
                           headers=headers,
                           data=userdata) as response:
            d = json.loads(response.text)   
            #d2 = response.text
            #print(d2)
            #return d.get('userInfo').get('token')
            return d.get('userInfo').get('ssoSessionid')
            #return d



if __name__ == '__main__':
    calss1 = Token()
    tk1 = calss1.Sessionid()
    print(tk1)
    
    
    
    
    
    