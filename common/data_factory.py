from api.common.business import Token
from api.common.excel_util import Excel
from api.config.config import Config
from api.common.yaml_util import RedYaml
from string import Template
import json
import time 


class PetData:

    @staticmethod
    def petTestCase(torow = None):
        '''
        # excel = Excel('D:/workspace/2021/webflash20/venv/api/data/testcases.xlsx')
        excel = Excel(Config().testCaseFile)
        excel.open()
        row =excel.get_rows_count()
        print(row)
        col =excel.get_columns_count()
        print(col)
        list =[]
        for i in range(1,row):
         for n in range(col):
             m = excel.get_cell_value1(i,n)
       # print(type(m))
             list.append(m)
        return list
        excel.close()
        '''
        excel = Excel(Config().testCaseFile)
        excel.open()
        if torow:
            lastrow = torow
        else:
            lastrow = excel.get_rows_count()

        data = excel.get_range_value('A2',f'M{lastrow}')
        excel.close()
        return data
    
    @staticmethod
    def petTestCaseJson():
        # json<-->dict
        # json.dump/json.dumps，json.load/json.loads
        # json.dumps  json.loads  --内存中对象转换
        # json.dump   json.load   --内存到文件之间的转换
        with open(Config().testCaseJsonFile, 'r', encoding='UTF-8') as f:
            data = json.load(f,strict=False)
            return data.get('data')

    @staticmethod
    def petTestCaseYaml(key_value=None):   
        """
        # yaml<-->dict 
        打开yaml
        :return:
        """
        yamlFile =RedYaml(Config().testCaseYamlFile)
        #print(yamlFile)

        data =RedYaml.get_key_value(yamlFile,key_value)
        #print(data)
        replace_data =Random_replace.temp_Random_replace(data)
        return replace_data['data']    
    
    @staticmethod
    def petTestApiKey():   
        """ 
        打开Config
        :return:
        """
        testApiKey =[]
        api_key = Config().testApiKey
        testApiKey.append(api_key)
        return testApiKey

    @staticmethod
    def petTestSessionid():   
        """ 
        打开Config
        :return:
        """
        session_list =[]
        session_id = Token().Sessionid()
        session_list.append(session_id)
        return session_list 

    @staticmethod
    def petTestUrl():   
        """ 
        打开Config
        :return:
        """
        urlList = []
        uatUrl =  Config().testUatUrl
        urlList.append(uatUrl)
        sitUrl =  Config().testSitUrl
        urlList.append(sitUrl)
        proUrl =  Config().testProUrl
        urlList.append(proUrl)
        return urlList 

    @staticmethod
    def petTestLongValue():   
        """ 
        打开Config
        :return:
        """
        longValue = []
        test501 =  Config().test501
        longValue.append(test501)
        test201 =  Config().test201
        longValue.append(test201)
        return longValue 
class CaseTitle:
    module = 0
    id = 1
    casename = 2
    url = 3
    method = 4
    params = 5
    headers = 6
    body = 7
    bodtype = 8
    status_code = 9
    message = 10
    result = 11
    tester = 12

class CaseTitleText:
    module = 'module'
    id = 'id'
    casename = 'casename'
    url = 'url'
    method = 'method'
    params = 'params'
    headers = 'headers'
    body = 'body'
    bodtype = 'bodytype'
    status_code = 'status_code'
    message = 'message'
    result = 'result'
    tester = 'tester'

class LoginData:
    @staticmethod
    def loginTestCase():
        # 数据存储格式：
        # 1、excel；2、json；3、yaml；4、xml
        data = [
            {'username': 'lizhen16', 'password': '123456', 'checkpoint': [{'resultCode': 200}, {'resultMessage': '成功'}]}
                ]
        return data


class DeptData:

    @staticmethod
    def format_simplename():
        """
        部门名称
        :return:
        """
        from mimesis import Business
        p = Business('zh')
        return p.company()

    @staticmethod
    def format_Numbers_between_init():
        """
        正整数
        :return:
        """
        from mimesis import Numbers
        n = Numbers()
        return n.between(1,100)

    @staticmethod
    def format_Datetime_week_date():
        """
        每年的第x周
        :return:
        """        
        from mimesis import Datetime
        d = Datetime()
        return d.week_date(2020,2021)
    
    @staticmethod
    def format_Datetime_time():
        """
        随机时分秒，例子：06:19:35
        :return:
        """           
        from mimesis import Datetime
        d = Datetime()
        return d.time()
    
    @staticmethod
    def format_Datetime_timestamp():
        """
        随机时间戳，例子：1131985278
        :return:
        """  
        from mimesis import Datetime
        d = Datetime()
        return d.timestamp() 
    
    @staticmethod
    def format_Internet_home_page():
        """
        随机网址，例子：http://www.molar.ao
        :return:
        """ 
        from mimesis import Internet
        d = Internet()
        return d.home_page() 
    
    @staticmethod
    def format_person_full_name():
        
        """
        随机英文全名，例子：Luci Norman
        :return:
        """ 
        from mimesis import Person
        d = Person()
        return d.full_name() 

    @staticmethod
    def format_person_email():
        """
        随机邮件地址，例子：burgesses1820@yandex.com
        :return:
        """         
        from mimesis import Person
        d = Person()
        return d.email()  
    
    @staticmethod
    def format_person_university():
        """
        随机大学，例子：Atlanta Metropolitan State College
        :return:
        """           
        from mimesis import Person
        d = Person()
        return d.university() 
    
    @staticmethod
    def format_person_telephone():
        """
        随机电话号码，例子：(001) 206-7173，805.538.4581
        :return:
        """        
        from mimesis import Person
        d = Person()
        return d.telephone() 




    @staticmethod
    def format_Cryptographic_uuid():
        """
        随机uuid，例子：36198665-3183-69f8-b7d2-0bd544eae5f0
        :return:
        """        
        from mimesis import Cryptographic
        d = Cryptographic()
        return d.uuid()

    @staticmethod
    def format_Cryptographic_hash():
        """
        随机哈希，例子：ac41b13e20f481647f9b69cf74c2b91649f5dc29
        :return:
        """        
        from mimesis import Cryptographic
        d = Cryptographic()
        return d.hash()

    @staticmethod
    def format_Business_price():
        """
        随机价格，例子：536.03 $
        :return:
        """        
        from mimesis import Business
        d = Business()
        return d.price()


class Random_replace:
    @staticmethod
    def temp_Random_replace(yaml_data):
        
        str_yaml_data = str(yaml_data)
        tempTemplate = Template(str_yaml_data)
        replace_business_name =Random_replace.temp_random_business_name()
        replace_university =Random_replace.temp_random_university()
        replace_email =Random_replace.temp_random_email()
        replace_full_name =Random_replace.temp_random_full_name()   
        replace_uuid =Random_replace.temp_random_uuid()  
        replace_int =Random_replace.temp_random_int()
        replace_timestamp =Random_replace.temp_random_timestamp()
        replace_url =PetData.petTestUrl()
        replace_sessionid=PetData.petTestSessionid()
        #replace_long_value =PetData.petTestLongValue()       
        replace_apiKey=PetData.petTestApiKey()
        random_string = {'name1': replace_business_name[0],'name2': replace_business_name[1],'name3': replace_business_name[2],'name4': replace_business_name[3]
                         ,'name5': replace_business_name[4],'name6': replace_business_name[5],'name7': replace_business_name[6],'name8': replace_business_name[7]
                         ,'name9': replace_business_name[8],'name10': replace_business_name[9],
                         'university1': replace_university[0],'university2': replace_university[1],'university3': replace_university[2],'university4': replace_university[3]
                         ,'university5': replace_university[4],'university6': replace_university[5],'university7': replace_university[6],'university8': replace_university[7]
                         ,'university9': replace_university[8],'university10': replace_university[9],
                          'email1': replace_email[0],'email2': replace_email[1],'email3': replace_email[2],'email4': replace_email[3]
                         ,'email5': replace_email[4],'email6': replace_email[5],'email7': replace_email[6],'email8': replace_email[7]
                         ,'email9': replace_email[8],'email10': replace_email[9],
                         'full_name1': replace_full_name[0],'full_name2': replace_full_name[1],'full_name3': replace_full_name[2],'full_name4': replace_full_name[3]
                         ,'full_name5': replace_full_name[4],'full_name6': replace_full_name[5],'full_name7': replace_full_name[6],'full_name8': replace_full_name[7]
                         ,'full_name9': replace_full_name[8],'full_name10': replace_full_name[9],
                         'uuid1': replace_uuid[0],'uuid2': replace_uuid[1],'uuid3': replace_uuid[2],'uuid4': replace_uuid[3]
                         ,'uuid5': replace_uuid[4],'uuid6': replace_uuid[5],'uuid7': replace_uuid[6],'uuid8': replace_uuid[7]
                         ,'uuid9': replace_uuid[8],'uuid10': replace_uuid[9],
                         'int1': replace_int[0],'int2': replace_int[1],'int3': replace_int[2],'int4': replace_int[3]
                         ,'int5': replace_int[4],'int6': replace_int[5],'int7': replace_int[6],'int8': replace_int[7]
                         ,'int9': replace_int[8],'int10': replace_int[9],
                         'timestamp1': replace_timestamp[0],'timestamp2': replace_timestamp[1],'timestamp3': replace_timestamp[2],'timestamp4': replace_timestamp[3]
                         ,'timestamp5': replace_timestamp[4],'timestamp6': replace_timestamp[5],'timestamp7': replace_timestamp[6],'timestamp8': replace_timestamp[7]
                         ,'timestamp9': replace_timestamp[8],'timestamp10': replace_timestamp[9],
                         'url': replace_url[0],'sessionid': replace_sessionid[0],'apiKey': replace_apiKey[0],'apiKey2': replace_apiKey[0]
                         }
        #print(replace_business_name)
        temp_replace =tempTemplate.safe_substitute(random_string)
        yaml_temp_replace = eval(temp_replace)
        #print(yaml_temp_replace,type(yaml_temp_replace))
        return yaml_temp_replace

    @staticmethod
    def temp_random_business_name():
        list_business_name  =[]
        rd =DeptData
        for i in range(10):
            ###随机10个不同类型的参数
            random_name =rd.format_simplename()
            random_time =time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
            random_New_name =random_name + str(random_time)
            ###把不同类型的参数加到list
            list_business_name.append(random_New_name)
            
        return list_business_name

        
    @staticmethod
    def temp_random_int():
        list_int =[]
        rd =DeptData
        for i in range(10):
            ###随机10个不同类型的参数
            random_int  =rd.format_Numbers_between_init()
            ###把不同类型的参数加到list
            list_int.append(random_int)
        return list_int  
    
    @staticmethod    
    def temp_random_uuid():
        list_uuid  =[]
        rd =DeptData
        for i in range(10):
            ###随机10个不同类型的参数
            random_uuid =rd.format_Cryptographic_uuid()
            ###把不同类型的参数加到list
            list_uuid.append(random_uuid)
        return list_uuid  

    @staticmethod   
    def temp_random_email():
        list_email =[]
        rd =DeptData
        for i in range(10):
            ###随机10个不同类型的参数
            random_email =rd.format_person_email()
            ###把不同类型的参数加到list
            list_email.append(random_email)
        return list_email
 
    @staticmethod
    def temp_random_full_name():
        list_full_name =[]
        rd =DeptData
        for i in range(10):
            ###随机10个不同类型的参数
            random_full_name =rd.format_person_full_name()
            ###把不同类型的参数加到list
            list_full_name.append(random_full_name)
        return list_full_name  
 
    
    @staticmethod    
    def temp_random_university():
        list_university =[]
        rd =DeptData
        for i in range(10):
            ###随机10个不同类型的参数
            random_university =rd.format_person_university()
            ###把不同类型的参数加到list
            list_university.append(random_university)
        return list_university  

    @staticmethod       
    def temp_random_timestamp():

        list_timestamp  =[]
        rd =DeptData
        for i in range(10):
            ###随机10个不同类型的参数
            random_time =rd.format_Datetime_timestamp()
            ###把不同类型的参数加到list
            list_timestamp.append(random_time)
        return list_timestamp  
    

    
if __name__ == '__main__':
    
    dep1 =DeptData()
    n1 = dep1.format_Business_price()
    print(n1)
    pet = PetData()
    p1 = pet.petTestCaseYaml('lili11')
    p2 = pet.petTestLongValue()
    print(p1)
    #p2 = pet.petTestSessionid()

    #print(len(p1),p1)
'''
    ss =p1
    s3= p1[0]
    s4=json.dumps(s3)
    print(type(s4),s4)
    #print(p2)

    ss ={"data":{"serviceName":"${name10}","serviceProvideDepartObj":{"name":"运营部","id":"1000000006","parentId":"1000000004",
              "subList":[{"name":"客户关系中心","id":"1000000007","parentId":"1000000006","subList":[]},
              {"name":"运营中心","id":"1000000010","parentId":"1000000006","subList":[]},
              {"name":"商业开发中心","id":"1000003534","parentId":"1000000006","subList":[]},
              {"name":"数字运营及主数据中心","id":"1000005777","parentId":"1000000006","subList":[]}]},"serviceObj":["1"],"serviceTypeObj":{"id":"60b760aee164026fd20a0c1c","name":"散包管理类"},
              "touchAccess":'false',"serviceSchema":" ces","serviceRequestAddress":"","serviceFormType":"1","serviceProviderObj":{},
              "serviceOnlineTime":"2021-07-23","serviceGuideAddress":"","serviceOwnerName":"吴**","serviceOwner":"wuyfeng","processGroupListName":"吴**",
              "processGroupList":["wuyj"],"labelName":["ss"],"formType2Val":"","labelList":[{"name":"ss"}],"serviceProvideDepartId":"1000000006",
              "serviceType":"60b760aee164026fd20a0c1c"}}

    a =Random_replace
    b =a.temp_random_business_name()
    c =a.temp_Random_replace(ss)
    print(b)
'''