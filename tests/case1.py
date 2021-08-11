import pytest
import json
#from api.common.httpclient import HttpClient
from api.common.run_method import RequestHandler
from api.common.data_factory import PetData
from api.common.data_factory import CaseTitle
from api.common.data_factory import CaseTitleText
from api.log.log import Log
import allure
@allure.feature('用户管理')   # 模块
class Login:
     @allure.story('登录功能')   # 功能
     @allure.title('测试用例标题') # 用例名称
     def test_login_001(self):

         pass
     def test_login_002(self):
         pass


class TestCase:

     @pytest.mark.v1
     @pytest.mark.parametrize('case', PetData.petTestCase())
     def test_case_excel(self, case):
        url=case[CaseTitle.url]
        headers =json.loads(case[CaseTitle.headers])
        #body =case[CaseTitle.body]        
        method=case[CaseTitle.method]
        case_status_code = int(case[CaseTitle.status_code])
        #bodytype=case[CaseTitle.bodtype]
        #params=case[CaseTitle.params]
        data =json.loads(case[CaseTitle.body])
        req = RequestHandler()
        client = req.visit(method, url, data,headers)
        response =json.loads(client.text)
        response_status_code = response.get('resultCode')
        print(response_status_code)
        print('------------------------------')        
        #print(send)
        print('------------------------------')
        print(url)
        print('------------------------------')       
        print(method)    
        print('------------------------------')
        print(type(data))
        print('------------------------------')
        print(type(headers))
        print('------------------------------')    
        print(case_status_code,type(case_status_code))
        print(response_status_code,type(response_status_code))       
        assert case_status_code == response_status_code
        #assert case[CaseTitle.message] == client.text       
        #client = HttpClient(url,headers,body,method,bodytype,params)
        '''
        if body is not None:
             client.set_body(json.loads(body))
        if headers is not None:
             client.headers = json.loads(headers)
        
        client.send()
        ss =client.response
        print('------------------------------')
        print(ss)
        print('------------------------------')
        print(url,headers,method,body,bodytype,params)


        '''
'''
    @allure.feature('ALM管理系统')
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
            client.set_body(json.loads(case[CaseTitleText.body]),strict=False)
        if case[CaseTitleText.headers] is not None:
            client.headers = json.loads(case[CaseTitleText.headers],strict=False) #strict=False,支持非标准json格式

        client.send()

        allure.dynamic.description(f'请求url：<font color=“red”>{case[CaseTitleText.url]}</font><br/>'
                                   f'期望状态码：{case[CaseTitleText.status_code]}，实际状态码：{client.status_code}<br/>'
                                   f'期望返回消息：{case[CaseTitleText.message]}')

        assert case[CaseTitleText.status_code] == client.resultCode
        assert case[CaseTitleText.message] == client.resultMessage

        # desc = f"<font color='red'>请求url：{case[CaseTitleText.url]}</font><br/>"
'''


if __name__ == '__main__':
    #pytest.main(['-m', 'v2', '-s'])
    #pytest.main(['/Users/longhuadmin/opt/anaconda3/lib/python3.8/site-packages/api/tests/test_case.py'])
    pytest.main(['-m', 'v1','-s','/Users/longhuadmin/opt/anaconda3/lib/python3.8/site-packages/api/tests/test_case.py','--html=./report/4.html'])
    
    #t = TestCase()
    #t1 = t.test_case_excel()
    
    
