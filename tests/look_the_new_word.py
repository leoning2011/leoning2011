#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 20:25:36 2021

@author: longhuadmin
"""
from string import Template
import json

ss ={"data":{"serviceName":"${name}","serviceProvideDepartObj":{"name":"运营部","id":"1000000006","parentId":"1000000004",
              "subList":[{"name":"客户关系中心","id":"1000000007","parentId":"1000000006","subList":[]},
              {"name":"运营中心","id":"1000000010","parentId":"1000000006","subList":[]},
              {"name":"商业开发中心","id":"1000003534","parentId":"1000000006","subList":[]},
              {"name":"数字运营及主数据中心","id":"1000005777","parentId":"1000000006","subList":[]}]},"serviceObj":["1"],"serviceTypeObj":{"id":"60b760aee164026fd20a0c1c","name":"散包管理类"},
              "touchAccess":'false',"serviceSchema":" ces","serviceRequestAddress":"","serviceFormType":"1","serviceProviderObj":{},
              "serviceOnlineTime":"2021-07-23","serviceGuideAddress":"","serviceOwnerName":"吴**","serviceOwner":"wuyfeng","processGroupListName":"吴**",
              "processGroupList":["wuyj"],"labelName":["ss"],"formType2Val":"","labelList":[{"name":"ss"}],"serviceProvideDepartId":"1000000006",
              "serviceType":"60b760aee164026fd20a0c1c"}}

s12 =ss['data']
#print(s12)
s13 = str(s12)
#print(type(s13))

tempTemplate = Template("My name is $name , i like $fancy")
d = {'name': 'yoyo', 'fancy': 'python'}
print(tempTemplate.substitute(d))



tempTemplate2 = Template("My name is ${name} , i like ${fancy}")
d2 = {'name': 'yoyo', 'fancy': 'python'}
print(tempTemplate2.substitute(d2))



tempTemplate3 = Template(s13)
d3 = {'name': 'yoyo','fancy': 'python'}
print()
s14 =tempTemplate3.safe_substitute(d3)
s15 = eval(s14)
print(s15,type(s15))

