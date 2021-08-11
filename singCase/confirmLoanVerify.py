#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Mu time:2021/7/27
from urllib.parse import urlencode

import requests
import json
headers={"Content-Type":"application/x-www-form-urlencoded"}
data={
  "code": "122371",
  "coreOrderNo": "1182244582104866816"
}

body={
    # 表单编码是用数据发送POST请求的常规方式。只需提供一个datadict；您甚至不需要指定内容类型。
    # 对于嵌套的json数据，需要将嵌套的json对象转换为字符串
    'data':json.dumps(data),
    'type':'3des',
    'arg':'m=cbc_pad=pkcs5_p=b2c17b46e2b1415392aab5a82869856d_i=61960860_o=0_s=utf-8_t=0'

}

r=requests.post(url="http://tool.chacuo.net/crypt3des/",data=body,headers=headers)
print(r.text)

Content-Length	206
Accept	*/*
X-Requested-With	XMLHttpRequest
User-Agent	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36
Content-Type	application/x-www-form-urlencoded; charset=UTF-8
Origin	http://tool.chacuo.net
Referer	http://tool.chacuo.net/crypt3des/
Accept-Encoding	gzip, deflate
Accept-Language	zh-CN,zh;q=0.9
Cookie	__yjs_duid=1_7322bf605c59ec7e996848187eb804ca1627476200280; Hm_lvt_ef483ae9c0f4f800aefdf407e35a21b3=1627476201; Hm_lpvt_ef483ae9c0f4f800aefdf407e35a21b3=1627476201; bdshare_firstime=1627476200826; __gads=ID=1f452a22179991bb-223ad45d90ca0018:T=1627476201:RT=1627476201:S=ALNI_MYHVxLfOKC5pEnyN0klRPcclv5xAQ
Connection	keep-alive