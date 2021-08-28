import json
import pytest
import requests

# 从数据工厂获取需要的登录测试用例数据
from api.common.data_factory import LoginData

class TestLogin:
    @pytest.mark.v2
    @pytest.mark.parametrize('user', LoginData.loginTestCase())
    def test_login(self, user):
        url = 'http://c2-uat-sso.######.com/doLogin'
        headers = {
            'Content-Type':'application/x-www-form-urlencoded',
               }
        userdata = {'username': user.get('username'), 'password': user.get('password')}

        with requests.post(url=url,
                           headers=headers,
                           data=userdata) as response:
            d = json.loads(response.text)
            checks = user.get('checkpoint')  # 第一条用例数据：checks=[{'code':9999},{'msg':'登录时失败'}]
            # 执行检查
            for item in checks:  # 遍历每个检查点
                for k, v in item.items():  # 遍历该检查点的期望值
                    assert d.get(k) == v  # d.get(k)---实际值，v---期望值
                    
 
                    
 
if __name__ == '__main__':
    pytest.main(['-s','test_login.py', '--html=/Users/.######./opt/anaconda3/lib/python3.8/site-packages/api/report/huice.html'])
    
                    
                    
