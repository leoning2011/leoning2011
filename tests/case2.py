import pytest
import json
from api.common.httpclient import HttpClient
from api.common.data_factory import PetData
from api.common.data_factory import CaseTitle
from api.common.data_factory import CaseTitleText

import allure
# @allure.feature('用户管理')   # 模块
# class Login:
#     @allure.story('登录功能')   # 功能
#     @allure.title('测试用例标题') # 用例名称
#     def test_login_001(self):
#
#         pass
#     def test_login_002(self):
#         pass


class TestCase:

     #@pytest.mark.v1
     #@pytest.mark.parametrize('case', PetData.petTestCase())
     #def test_case_excel(self, case):
 
         #case_url=case[CaseTitle.url]
         #case_method=case[CaseTitle.method]
         #case_bodytype=case[CaseTitle.bodtype] 
         #case_params=json.loads(case[CaseTitle.params])
         #case_body =json.loads(case[CaseTitle.body])
         #case_headers =json.loads(case[CaseTitle.headers])
         #case_status_code =int(case[CaseTitle.status_code])
         #case_message =case[CaseTitle.message]
         
         #print(case_url,type(case_url))
         #print(case_method,type(case_method))    
         #print(case_bodytype,type(case_bodytype))
         #print(case_params,type(case_params)) 
         #print(case_body,type(case_body))
         #print(case_headers,type(case_headers))         
         #print(case_status_code,type(case_status_code))
         #print(case_message,type(case_message))          
         
         #client = HttpClient(url=case_url,
                             #method=case_method,
                             #bodytype=case_bodytype,
                             #params=case_params) 
       
              
    
         #s1 = client.send()
         
         #print(s1,type(s1))          
         #assert case_status_code == s1
         #assert case_message == client.text

    @allure.feature('alm管理系统')
    @pytest.mark.v2
    @pytest.mark.parametrize('case', PetData.petTestCaseJson())
    def test_case_json(self, case):
        # 设置相关标题
        allure.dynamic.story(case[CaseTitleText.module])
        allure.dynamic.title(case[CaseTitleText.casename])

        client = HttpClient(url=case[CaseTitleText.url],
                            method=case[CaseTitleText.method],
                            bodytype=case[CaseTitleText.bodtype],
                            params=case[CaseTitleText.params])

        if case[CaseTitleText.body] is not None:
            client.set_body(json.loads(case[CaseTitleText.body]))
        if case[CaseTitleText.headers] is not None:
            client.headers = json.loads(case[CaseTitleText.headers])

        client.send()

        allure.dynamic.description(f'请求url：<font color=“red”>{case[CaseTitleText.url]}</font><br/>'
                                   f'期望状态码：{case[CaseTitleText.status_code]}，实际状态码：{client.status_code}<br/>'
                                   f'期望返回消息：{case[CaseTitleText.message]}')

        assert case[CaseTitleText.status_code] == client.status_code
        assert case[CaseTitleText.message] == client.text

        # desc = f"<font color='red'>请求url：{case[CaseTitleText.url]}</font><br/>"



if __name__ == '__main__':
    pytest.main(['-m', 'v2','-s','/Users/longhuadmin/opt/anaconda3/lib/python3.8/site-packages/api/tests/test_case2.py','--html=./report/4.html'])
    