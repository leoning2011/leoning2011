#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 12:18:06 2021

@author: ningxinghua
"""

import requests
import json
import time
import urllib3


#获取session
def ssoSession(username,password):
    url = 'http://c2-uat-sso.longfor.com/doLogin'
    headers = {
               'Content-Type':'application/x-www-form-urlencoded',
               }

    
    userdata = {'username': username, 'password': password}
    with requests.post(url=url,
                       headers=headers,
                       data=userdata) as response:
        d = json.loads(response.text)   
        #d2 = response.text
        #print(d2)
        #return d.get('userInfo').get('token')
        return d.get('userInfo').get('ssoSessionid')






#创建项目接口
def Creat_project(ssoSessionid):
    url = 'http://10.231.141.60:9000/alm/mdm/new/emp'
    headers = {
                'Content-Type':'application/json',
                'x-gaia-api-key':'d6b00510-4549-4a05-bf37-fe7e7da9a1a3',
                'c2-sso-sessionid':ssoSessionid
               }
    userdata ={
        "SystemID":"ALM","PJ_NAME":"ALM","TY_NAME":"MD059B","PJ_TYPE":"ZO","ItemArray":
         [
        	{"EMPLOYEEP":100124656,"CROSSPOS":0,"KEYLEADER":"tonghao","ORGOWNER":"liju,yangdan61",
          "CHANNEL":"LF03","CHANNELNM":"C4","STATUS":"A","POSCODE":10028461,
          "POSNAME":"管家中心-管家员工","POSDESC":"管家中心-管家员工","LOCATION":"CHENGDU",
          "LOCADESC":"成都","JOBCODE":50262,"JOBNAME":"管家员工",
          "JOBDESC":"管家员工","JOBID":"1G","JOBIDDESC":"员工",
          "FIRSTID":"2T","FIRSTDES":"管家","SECONDID":"8L",
          "SECONDDES":"管家","THIRDID":"6N",
          "THIRDDES":"管家","ORGID":1000006683,
          "SYSFLAG":"DC","CREATEDAT":"2021-07-10 09:25:58",
          "UPDATEDAT":"2021-07-10 09:25:58","KEYLEADDS":"童浩",
          "ORGOWNERD":"李菊,杨丹",
          "POSCODEUP":"10032971,10032971",
          "EMP_COMP":1000001528,"DEPID_FI":1000000071,"DEPID_SE":1000000073
           }]}
            
    
    with requests.post(url=url,
                       headers=headers,
                       data=userdata,verify=False) as response:
        d = json.loads(response.text)   
        #d2 = response.text
        #print(d2)
        #return d.get('userInfo').get('token')
        
        return d




if __name__ == '__main__':


    urllib3.disable_warnings()
    #登录系统,获取sessionid
    ss1 = ssoSession('lizhen16','123456')
    time.sleep(3)
    print(ss1)
    print('用户登录完成,请检查用户登录状态')
    #创建项目,并获取项目id
    ss2 =Creat_project(ss1)
    print(ss2)

    
    
    

