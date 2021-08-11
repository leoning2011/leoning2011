#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 09:01:38 2021

@author: longhuadmin
"""

import requests
import json
import httpx
from api.log.log import logger

class Method:
    GET = 'get'
    POST = 'post'
    DELETE = 'delete'
    PUT = 'put'

class BodyType:
    FORM_DATA = 'multipart/form-data'
    JSON = 'application/json'
    XML = 'application/xml'
    URL_ENCODE = 'application/x-www-form-urlencoded'



class Client:

    def run_http(method,url,headers,data):  
        try:
            if method.upper()=='GET':
               with requests.get(url=url,
                           headers=headers,
                           data=data,verify=False) as response: 
                    data = json.loads(response.text)
                    return data
            if method.upper()=='POST':
               with requests.post(url=url,
                           headers=headers,
                           data=data,verify=False) as response: 
                    data = json.loads(response.text)
                    return data
        except Exception as r :
            print('异常错误 %s' %r) 
            logger.error(r)
          
if __name__ == '__main__':
    # 以下是测试代码
    # post请求接口
    method ='post'
    url = 'http://c2-uat-sso.longfor.com/doLogin'
    data = {
        "username": "lizhen16",
        "password": "12"
    }
    headers = {
            'Content-Type':'application/x-www-form-urlencoded',
               }
    #s1 =Client
    #s2 =s1.run_http(method=method,url=url,headers=headers,data=data)
     
    print(method,type(method))    
    print(url,type(url))
    print(data,type(data)) 
    print(headers,type(headers)) 
    with requests.post(url=url,
                       headers=headers,
                       data=data) as result:
        s =result
    print(s)