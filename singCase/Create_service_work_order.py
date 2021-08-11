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
                'Content-Length':'169',
                'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
                'Content-Type':'application/x-www-form-urlencoded',
                'Origin':'http://c2-uat-sso.longfor.com',
                'Referer':'http://c2-uat-sso.longfor.com/?redirect_url=68747470733a2f2f636d2d616c6d2d746573742e6c6f6e67666f722e636f6d2f70726f6a6563742f63656e7465722f31303030303036303736',
                'Accept-Encoding':'gzip, deflate',
                'Accept-Language':'zh-CN,zh;q=0.9',
                'Cookie':'zgclear=true',
                'Connection':'keep-alive'
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
    url = 'https://testapi.longhu.net/cm-alm-manage-admin-uat/alm/service/manage/save'
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
        "serviceFormType": '1', 
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
    
    
    print(type(userdata))
    print(type(userdata))
    with requests.post(url=url,
                       headers=headers,
                       data=json.dumps(userdata),verify=False) as response:
       d = json.loads(response.text)   
       return d     


#新建定制工单
def Service_work_order2(ssoSessionid,Service_work_name,RequestAddress):
    url = 'https://testapi.longhu.net/cm-alm-manage-admin-uat/alm/service/manage/save'
    headers = {
                'Content-Type':'application/json',
                'x-gaia-api-key':'d6b00510-4549-4a05-bf37-fe7e7da9a1a3',      
                'c2-sso-sessionid':ssoSessionid
               }
    userdata =  {
    "data": {
        "serviceName": ordername, 
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
        "serviceSchema": "测试", 
        "serviceRequestAddress": RequestAddress, 
        "serviceFormType": "2", 
        "serviceProviderObj": { }, 
        "serviceOnlineTime": "2021-06-22", 
        "serviceGuideAddress": "", 
        "serviceOwnerName": "张**", 
        "serviceOwner": "zhangxinghua", 
        "processGroupListName": "王**", 
        "processGroupList": [
            "wanggang4"
        ], 
        "labelName": [
            "阿斯顿发个"
        ], 
        "formType2Val": "mdm", 
        "labelList": [
            {
                "name": "阿斯顿发个"
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





if __name__ == '__main__':
    
    wait = 2
    list1 = ['mdm','idm','bpm','am','contact','i','ami','scrum']
    urllib3.disable_warnings()
    #登录系统,获取sessionid
    for i in range(1):
       for n in range(len(list1)):
        RequestAddress= list1[n]    
        time2 =time.strftime('%H%M%S',time.localtime(time.time()))
        random_name = DeptData().simplename()
        print(random_name)
        sessionid = SsoSession('wanggang4','12')
        time.sleep(wait)
        print(sessionid)   
        #serviceFormType = 2 #1,标准工单   2,定制工单  3,第三方
        #Service_work_name =DeptData
        #Service_work_type ='标准工单22'
        #Service_work_name =Service_work.simplename()
        #Service_work_name_full_name =Service_work_type + Service_work_name
        #print(Service_work_name_full_name)  
        #Service_work_name = '标准' + random_name
        ordername =RequestAddress  + str(random_name)  +str(time2)
        #order1 = Service_work_order(sessionid,Service_work_name)
        print(ordername)
        order2 = Service_work_order2(sessionid,ordername,RequestAddress)  
        '''
        主数据服务  mdm
        IDM账号管理登录认证    idm
        BPM流程审批接入   bpm
        AM权限平台接入   am
        触点平台申请应用权限  contact
        小i接入申请   i
        敏捷成熟度实施服务申请    ami
        敏捷服务申请 scrum
        '''
        time.sleep(wait)
        #print(order1)
        print(order2)
        #del (Service_work_name_full_name)
        print('工单新建完成+1')

      
 

