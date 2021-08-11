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
    
#通过子项目反查项目信息
def Project_information(ssoSessionid,Sub_Project_name):
    url = 'https://testapi.longhu.net/cm-alm-manage-admin-uat/alm/dt/center/subProject/list'
    headers = {
                'Content-Type':'application/json',
                'x-gaia-api-key':'d6b00510-4549-4a05-bf37-fe7e7da9a1a3',      
                'c2-sso-sessionid':ssoSessionid
               }
    userdata =  {
	"data": {
		"developType": [],
		"healthyStatus": [],
		"subProjectCodeOrName": Sub_Project_name,
		"subProjectStatus": ["1"],
		"currentMileStone": "",
		"rdCenter": ""
	},
	"pageInfo": {
		"pageNum": 1,
		"pageSize": 30
	}
    }
    
    with requests.post(url=url,
                       headers=headers,
                       data=json.dumps(userdata),verify=False) as response:
       d = json.loads(response.text)   
       data = d.get('data')   
    return data     

#通过子项目反查产品信息
def Product_information(ssoSessionid,projectId):
    url = 'https://testapi.longhu.net/cm-alm-manage-admin-uat/alm/procurement/subProject/list'
    headers = {
                'Content-Type':'application/json',
                'x-gaia-api-key':'d6b00510-4549-4a05-bf37-fe7e7da9a1a3',      
                'c2-sso-sessionid':ssoSessionid
               }
    userdata = {
        "data":{"keyWord":"","projectId":projectId}
        }
    
    with requests.post(url=url,
                       headers=headers,
                       data=json.dumps(userdata),verify=False) as response:
       d = json.loads(response.text)   
       data = d.get('data') 
       
       return data


#获取项目所剩余金额
#
#通过子项目反查所剩资金
def Product_cost(ssoSessionid,projectId):
    url = 'https://testapi.longhu.net/cm-alm-manage-admin-uat/alm/procurement/project/remain/cost'
    headers = {
                'Content-Type':'application/json',
                'x-gaia-api-key':'d6b00510-4549-4a05-bf37-fe7e7da9a1a3',      
                'c2-sso-sessionid':ssoSessionid
               }
    userdata = {
	"data": {"projectId": projectId}
            }          
    
    with requests.post(url=url,
                       headers=headers,
                       data=json.dumps(userdata),verify=False) as response:
       d = json.loads(response.text)   
       return d.get('data')


#采购管理第一步,创建基础信息
def Creat_purchas_1(SsoSessionid,productId,projectId,subProjectId,Product_cost):
    url = 'https://testapi.longhu.net/cm-alm-manage-admin-uat/alm/procurement/save/base'
    headers = {
                'Content-Type':'application/json',
                'x-gaia-api-key':'d6b00510-4549-4a05-bf37-fe7e7da9a1a3',
                
                'c2-sso-sessionid':SsoSessionid
               }
    userdata =  {
	"data": {
		"type": "1",
		"bidAgentOa": "chenxiaolong1",
		"bidEvaluationPrinciple": "1",
		"bidModel": "1",
		"bidTheme": "神州发射成功",
		"bidWay": "1",
		"companyConfirmFiles": [],
		"expectCost": 3.01,
		"instructionsFiles": [{
			"id": 3027501,
			"name": "synapse-import-configuration-1612274974677.txt",
			"url": "http://c2-uat-sso-lf-files.longfor.com/files/fileDownload?fileUrl=056f446d2b241b6c9f35bcdd5009f15b",
			"urlPath": "http://c2-uat-sso-lf-files.longfor.com/files/fileDownload?fileUrl=056f446d2b241b6c9f35bcdd5009f15b",
			"uid": 1623898065842,
			"status": "success"
		}],
		"payMilestone": "1",
		"productId": productId,
		"projectId": projectId,
		"subProjectId": subProjectId,
		"providerBidDays": 5,
		"reason": "",
		"remainTargetCost": Product_cost,
		"securityProposal": "安全测试",
		"shortlistedMinNumber": '3',
		"toWinBidNumber": '1',
		"category": "022902",
		"whetherInvolveSecurityPrivacy": '1',
		"communicateFiles": []
        }
    }
            
    
    with requests.post(url=url,
                       headers=headers,
                       data=json.dumps(userdata),verify=False) as response:
        d = json.loads(response.text)   
        #d2 = response.text
        #print(d2)
        #return d.get('userInfo').get('token')
        
        return d
    
if __name__ == '__main__':

    wait = 2
    urllib3.disable_warnings()
    #登录系统,获取sessionid
    sessionid = SsoSession('wanggang4','12')
    time.sleep(wait)
    print(sessionid)
    print('用户登录完成,请检查用户登录状态')    
    Product = Project_information(sessionid,'江南天街')   #通过子项目反查,项目id,反查子项目id
    print(Product)
    time.sleep(wait)
    #data = Product.get('data')      #获取项目信息
    projectId = Product[0].get('projectId')   #获取项目id
    print(projectId)
    subProjectId = Product[0].get('subProjectId')   #获取子项目id
    print(subProjectId)
    time.sleep(wait)
    Product = Product_information(sessionid,projectId)     #获取产品信息
    productId = Product[0].get('productId')
    print(productId)    
    time.sleep(wait)
    Product_cost = Product_cost(sessionid,projectId)        #获取项目所剩余资金
    print(Product_cost) 
    time.sleep(wait)
    Creat_purchas_1 = Creat_purchas_1(sessionid,productId,projectId,subProjectId,Product_cost)
    print(Creat_purchas_1)
