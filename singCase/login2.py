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
def Creat_project(ssoSessionid,projectName):
    url = 'https://testapi.longhu.net/cm-alm-manage-admin-uat/alm/project/addOrUpdateProject'
    headers = {
                'Content-Type':'application/json',
                'x-gaia-api-key':'d6b00510-4549-4a05-bf37-fe7e7da9a1a3',
                
                'c2-sso-sessionid':ssoSessionid
               }
    userdata =  {
    "data": {
        "isMakeAmends": 0, 
        "projectName": projectName, 
        "bpoName": "李*", 
        "bpo": "100124656", 
        "bpoList": [
            {
                "id": 'null', 
                "name": "李*", 
                "account": "lizhen16", 
                "employeeId": "100124656", 
                "department": "", 
                "departmentShortName": "", 
                "personType": 1, 
                "quit": 'false', 
                "roleId": 'null', 
                "roleName": 'null', 
                "centerInfoList": 'null', 
                "superiorName": 'null', 
                "superior": 'null', 
                "payRdCenter": 'null', 
                "payRdCenterName": 'null', 
                "assignRate": 'null', 
                "rdCenter": "1000006076", 
                "centerName": "项目管理中心", 
                "role": "BPO", 
                "oaAccount": "lizhen16", 
                "teamUserId": "100124656", 
                "teamUserName": "李*"
            }
        ], 
        "tpoName": "李*", 
        "tpo": "100124656", 
        "tpoList": [
            {
                "id": 'null', 
                "name": "李*", 
                "account": "lizhen16", 
                "employeeId": "100124656", 
                "department": "", 
                "departmentShortName": "", 
                "personType": 1, 
                "quit": 'false', 
                "roleId": 'null', 
                "roleName": 'null', 
                "centerInfoList": 'null', 
                "superiorName": 'null', 
                "superior": 'null', 
                "payRdCenter": 'null', 
                "payRdCenterName": 'null', 
                "assignRate": 'null', 
                "rdCenter": "1000006076", 
                "centerName": "项目管理中心", 
                "role": "TPO", 
                "oaAccount": "lizhen16", 
                "teamUserId": "100124656", 
                "teamUserName": "李*"
            }
        ], 
        "sdmName": "李*", 
        "sdm": "100124656", 
        "sdmList": [
            {
                "id": 'null', 
                "name": "李*", 
                "account": "lizhen16", 
                "employeeId": "100124656", 
                "department": "", 
                "departmentShortName": "", 
                "personType": 1, 
                "quit": 'false', 
                "roleId": 'null', 
                "roleName": 'null', 
                "centerInfoList": 'null', 
                "superiorName": 'null', 
                "superior": 'null', 
                "payRdCenter": 'null', 
                "payRdCenterName": 'null', 
                "assignRate": 'null', 
                "rdCenter": "1000006076", 
                "centerName": "项目管理中心", 
                "role": "SDM", 
                "oaAccount": "lizhen16", 
                "teamUserId": "100124656", 
                "teamUserName": "李*"
            }
        ], 
        "approvalLevel": "1", 
        "departmentName": "北京地区", 
        "department": "1000000801", 
        "center": "1000006076", 
        "description": "测试", 
        "userList": [
            {
                "id": 'null', 
                "name": "李*", 
                "account": "lizhen16", 
                "employeeId": "100124656", 
                "department": "", 
                "departmentShortName": "", 
                "personType": 1, 
                "quit": 'false', 
                "roleId": 'null', 
                "roleName": 'null', 
                "centerInfoList": 'null', 
                "superiorName": 'null', 
                "superior": 'null', 
                "payRdCenter": 'null', 
                "payRdCenterName": 'null', 
                "assignRate": 'null', 
                "rdCenter": "1000006076", 
                "centerName": "项目管理中心", 
                "role": "TPO", 
                "oaAccount": "lizhen16", 
                "teamUserId": "100124656", 
                "teamUserName": "李*"
            }, 
            {
                "id": 'null', 
                "name": "李*", 
                "account": "lizhen16", 
                "employeeId": "100124656", 
                "department": "", 
                "departmentShortName": "", 
                "personType": 1, 
                "quit": 'false', 
                "roleId": 'null', 
                "roleName": 'null', 
                "centerInfoList": 'null', 
                "superiorName": 'null', 
                "superior": 'null', 
                "payRdCenter": 'null', 
                "payRdCenterName": 'null', 
                "assignRate": 'null', 
                "rdCenter": "1000006076", 
                "centerName": "项目管理中心", 
                "role": "BPO", 
                "oaAccount": "lizhen16", 
                "teamUserId": "100124656", 
                "teamUserName": "李*"
            }, 
            {
                "id": 'null', 
                "name": "李*", 
                "account": "lizhen16", 
                "employeeId": "100124656", 
                "department": "", 
                "departmentShortName": "", 
                "personType": 1, 
                "quit": 'false', 
                "roleId": 'null', 
                "roleName": 'null', 
                "centerInfoList": 'null', 
                "superiorName": 'null', 
                "superior": 'null', 
                "payRdCenter": 'null', 
                "payRdCenterName": 'null', 
                "assignRate": 'null', 
                "rdCenter": "1000006076", 
                "centerName": "项目管理中心", 
                "role": "SDM", 
                "oaAccount": "lizhen16", 
                "teamUserId": "100124656", 
                "teamUserName": "李*"
            }]}}  
            
    
    with requests.post(url=url,
                       headers=headers,
                       data=json.dumps(userdata),verify=False) as response:
        d = json.loads(response.text)   
        #d2 = response.text
        #print(d2)
        #return d.get('userInfo').get('token')
        
        return d.get('data').get('projectId')



#查询接口
def select1(ssoSessionid):
    url = 'https://testapi.longhu.net/cm-alm-manage-admin-uat/alm/project/centerList'
    headers = {
                'Content-Type':'application/json',
                'x-gaia-api-key':'d6b00510-4549-4a05-bf37-fe7e7da9a1a3',
                'c2-sso-sessionid':ssoSessionid
               }

    #userdata = {"data":{"type":3}}
    with requests.post(url=url,
                       headers=headers,verify=False
                       ) as response:
        d = json.loads(response.text)   
        #d2 = response.text
        #print(d2)
        #return d.get('userInfo').get('token')
        return d

##项目申请立项
def projectApproval(ssoSessionid,projectId):
    url = 'https://testapi.longhu.net/cm-alm-manage-admin-uat/alm/project/projectApproval'
    headers = {
                'Content-Type':'application/json',
                'x-gaia-api-key':'d6b00510-4549-4a05-bf37-fe7e7da9a1a3',
                'c2-sso-sessionid':ssoSessionid
               }

    data = {
	"data": {
		"files": [{
			"id": 44444,
			"name": "《首先,打破一切常规》电子版.pdf",
			"url": ""
		}],
		"strategicLevel": "0",
		"targetCost": 200,
		"priorityLevel": "A",
		"projectApprovalTime": "2021-06-09",
		"description": "测试",
		"projectId": projectId
	}
}
    with requests.post(url=url,
                       headers=headers,data=json.dumps(data),verify=False
                       ) as response:
        d = json.loads(response.text)   
        #d2 = response.text
        #print(d2)
        #return d.get('userInfo').get('token')
        return d


##获取审批流
def bpm_login(ssoSessionid,projectId):
    url = 'http://bpm3s.longfor.uat:8088/bpm-server/api/user/?datetime2=1623832727388'
    headers = {
                'Content-Type':'application/json',
                'x-gaia-api-key':'d6b00510-4549-4a05-bf37-fe7e7da9a1a3',
                'c2-sso-sessionid':ssoSessionid,
                'EagleEye-TraceID': '2a8e297172694d9eab52a87479a63049'
               }

    data = {
	"data": {
		"files": [{
			"id": 44444,
			"name": "《首先,打破一切常规》电子版.pdf",
			"url": ""
		}],
		"strategicLevel": "0",
		"targetCost": 200,
		"priorityLevel": "A",
		"projectApprovalTime": "2021-06-09",
		"description": "测试",
		"projectId": projectId
	}
}
    with requests.get(url=url,
                       headers=headers,data=json.dumps(data),verify=False
                       ) as response:
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
    ss2 =Creat_project(ss1,'江南测试项903')
    print(ss2)
    print('新增项目成功,请检查项目状态')
    time.sleep(3)
    #根据项目id,发起项目审批
    ss3 =projectApproval(ss1,ss2)
    #ss3 =projectApproval('1901725_8892f77b68c245e98f6b01471ebbb6a8',251458)
    print(ss3)
    print('项目发起审批完成,请检查状态')
    time.sleep(3)
    print()
    
    
    
    

