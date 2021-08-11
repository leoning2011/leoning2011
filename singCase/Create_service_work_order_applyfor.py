#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 10:06:46 2021

@author: longhuadmin
"""

import requests
import json
import time
import urllib3
from api.common.data_factory import DeptData



#获取session
def SsoSession(username,password):
    url = 'http://c2-uat-sso.longfor.com/doLogin'
    headers = {
        'Content-Type':'application/x-www-form-urlencoded'
               }

    
    userdata = {'username': username, 'password': password}
    with requests.post(url=url,
                       headers=headers,
                       data=userdata) as response:
        d = json.loads(response.text)   
        #d2 = response.text
        #print(d2)
        #return d.get('userInfo').get('ssoSessionid')
        return d.get('userInfo').get('ssoSessionid')
    
#新建标准工单
def Service_work_order(ssoSessionid,Service_work_name):
    url = 'https://testapi.longhu.net/cm-alm-manage-admin-uat/alm/service/manage/list'
    headers = {
                'Content-Type':'application/json',
                'x-gaia-api-key':'d6b00510-4549-4a05-bf37-fe7e7da9a1a3',      
                'c2-sso-sessionid':ssoSessionid
               }
    userdata =  {
    "data": {
        "serviceName": Service_work_name, 
        "serviceProvideDepartObj": {
            "name": "总经理室", 
            "id": "1000000005", 
            "parentId": "1000000004", 
            "subList": [ ]
        }, 
        "serviceObj": [
            "1"
        ], 
        "serviceTypeObj": {
            "id": "60b760ace164026fd20a0c0f", 
            "name": "数据获取类"
        }, 
        "touchAccess": 'false', 
        "serviceSchema": "测试0001", 
        "serviceRequestAddress": "", 
        "serviceFormType": "1", 
        "serviceProviderObj": { }, 
        "serviceOnlineTime": "2021-06-18", 
        "serviceGuideAddress": "", 
        "serviceOwnerName": "张**", 
        "serviceOwner": "zhangxinghua", 
        "processGroupListName": "王**", 
        "processGroupList": [
            "wanggang4"
        ], 
        "labelName": [
            "60b849a97540506c45839183", 
            "标准化功能"
        ], 
        "formType2Val": "", 
        "labelList": [
            {
                "id": "60b849a97540506c45839183", 
                "name": "测试", 
                "validStatus": 1
            }, 
            {
                "name": "标准化功能"
            }
        ], 
        "serviceProvideDepartId": "1000000005", 
        "serviceType": "60b760ace164026fd20a0c0f"
    }
}
    
    with requests.post(url=url,
                       headers=headers,
                       data=json.dumps(userdata),verify=False) as response:
       d = json.loads(response.text)   
       return d     

   
#服务申请
def Service_work_order_applyfor(ssoSessionid,serverno):
    url = 'http://10.231.139.246:8090/itsm/open-api/almServiceApplication/almServiceApplicationCreate'
    headers = {
                'Content-Type':'application/json',
                'x-gaia-api-key':'d6b00510-4549-4a05-bf37-fe7e7da9a1a3',      
                'c2-sso-sessionid':ssoSessionid
               }
    userdata =  {
    "schoolPersonnel": "", 
    "functionMenu": "", 
    "applicationParticulars": "测试", 
    "customType": "standard", 
    "almCode": 'null', 
    "productId": "223229", 
    "applicantAppName": "驼舟", 
    "applicantAppId": "PRD00008", 
    "applicantProdTpo": "孙*(sunpeng6),章*(zhangli)", 
    "applicantProdSdm": "扈*(hufang)", 
    "applicantProdBpo": "李*(lizhen16),赵*(zhaobo6)", 
    "applicantSubName": "6月24日", 
    "applicantSubProj": "XM1900124", 
    "applicationName": "", 
    "applicationId": "", 
    "applicationPrincipal": "", 
    "expectedCompletionDate": "2021-06-18", 
    "isNewApp": "2", 
    "applicantSubProj_1": "XM1900124", 
    "serviceNum": serverno, 
    "applicant": "李臻", 
    "userId": "lizhen16", 
    "serviceApplicant": "李臻(lizhen16)", 
    "isDraft": 'false'
}
    
    with requests.post(url=url,
                       headers=headers,
                       data=json.dumps(userdata),verify=False) as response:
       d = json.loads(response.text)   
       return d   
    
if __name__ == '__main__':

 
    wait = 2
    urllib3.disable_warnings()
    #登录系统,获取sessionid
    for i in range(573,658):
        time2 =time.strftime('H%M%S',time.localtime(time.time()))
        sessionid = SsoSession('wanggang4','12')
        time.sleep(wait)
        print(sessionid)
        serverno ='SERV0' + str(i)
        print(serverno)
        #Service_work_name =DeptData
        #Service_work_type ='标准工单22'
        #Service_work_name =Service_work.simplename()
        #Service_work_name_full_name =Service_work_type + Service_work_name
        #print(Service_work_name_full_name)         
        order = Service_work_order_applyfor(sessionid,serverno)
        time.sleep(wait)
        print(order)
        #del (Service_work_name_full_name)
      

      
 

