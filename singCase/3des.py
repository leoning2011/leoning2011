#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 20:59:29 2021

@author: longhuadmin
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Mu time:2021/7/27
from urllib.parse import urlencode

import requests
import json

url="http://tool.chacuo.net/crypt3des/"
headers={"Content-Type":"application/x-www-form-urlencoded"}

body={
    # 表单编码是用数据发送POST请求的常规方式。只需提供一个datadict；您甚至不需要指定内容类型。
    # 对于嵌套的json数据，需要将嵌套的json对象转换为字符串
    "data":{
            "code": "122371",
            "coreOrderNo": "1182244582104866816"
          },
    'type':'3des',
    'arg':'m=cbc_pad=pkcs5_p=b2c17b46e2b1415392aab5a82869856d_i=61960860_o=0_s=utf-8_t=0'
}
body2=json.dumps(body)
print(body2,type(body2))
with requests.post(url=url,
                  headers=headers,
                           data=body) as response:
            d = json.loads(response.text)  

print(d)


