import pytest
import json
import requests
from api.common.data_factory import PetData
from api.common.data_factory import DeptData
from api.common.data_factory import CaseTitle
from api.common.data_factory import CaseTitleText
from api.common.httpclient import Client
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


class TestYamlCase:

    @allure.feature('alm管理系统')
    @pytest.mark.v2
    @pytest.mark.parametrize('case', PetData.petTestCaseYaml('ningxinghua11'))
    def test_case_yaml(self, case):
        #rangdom_service_name =DeptData.format_simplename()
        #ssoSessionid =PetData.petTestSessionid()
        #print(ssoSessionid,type(ssoSessionid))
        #print(case,type(case))
        #case =json.loads(case)
        method =case[CaseTitleText.method]
        url  =case[CaseTitleText.url]
        head =case[CaseTitleText.headers][0]
        data =json.dumps(case[CaseTitleText.body])
        case_status_code =case[CaseTitleText.status_code]
        case_status_message = case[CaseTitleText.message] 
        #apiKey =PetData.petTestCaseYaml()
        #print(apiKey,type(apiKey))
        #print(Session,type(Session))
        print('-------------------------method--------------------')
        print(method,type(method))
        print('--------------------------url----------------------')
        print(url,type(url))
        print('--------------------------head---------------------')
        print(head,type(head))
        print('--------------------------body---------------------')
        #json_body =json.loads(data)
        #serviceName =json_body['data']
        #serviceName.update({'serviceName':rangdom_service_name})
        print(case[CaseTitleText.body],type(data))
        #print(serviceName,type(serviceName))
        #update_servicename =data['serviceName']
        #print(update_servicename,type(update_servicename))
        #body2= json.dumps(data)  
        #print(body2,type(body2))
        print('------------------case_status_code-----------------')
        print(case_status_code,type(case_status_code))
        print('------------------case_status_message--------------')        
        print(case_status_message,type(case_status_message))
        
        client = Client
        res = client.run_http(method =method,
                           url =url,
                           headers =head,  
                           data =data)
        print(res,type(res))
        resultCode= res['code']
        resultMessage =res['msg']
        print('----------------------resultCode--------------------')
        print(resultCode,type(resultCode))
        print('----------------------resultMessage-----------------')        
        print(resultMessage,type(resultMessage))
        #print(resultMessage)
        assert case_status_code == resultCode
        assert case_status_message == resultMessage



if __name__ == '__main__':
    #pytest.main(['-m', 'v1', '-s'])
    pytest.main(['-m', 'v2','-s','/Users/longhuadmin/opt/anaconda3/lib/python3.8/site-packages/api/tests/test_yaml.py','--html=/Users/longhuadmin/opt/anaconda3/lib/python3.8/site-packages/api/report/4.html'])
    #c1 =TestYamlCase().test_case_yaml(PetData.petTestCaseYaml('test_user_login'))
    #print(c1)
 