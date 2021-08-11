import configparser
import threading
import re
class Config:
    # __new__ 用于创建实例，而__init__用于初始化实例
    __configfile = r'/Users/longhuadmin/opt/anaconda3/lib/python3.8/site-packages/api/config/config.ini'
    __flag = False
    __instance_lock = threading.Lock() # 定义一把锁

    def remove_BOM(config_path):
        content = open(config_path).read()
        content = re.sub(r"\xfe\xff","", content)
        content = re.sub(r"\xff\xfe","", content)
        content = re.sub(r"\xef\xbb\xbf","", content)
        content = re.sub(r"\ufeff","", content)
        open(config_path, 'w').write(content)

    def __init__(self):
        # 如果配置初始化已经完成，直接返回
        if Config.__flag:
            return

        config = configparser.ConfigParser()
        config.read(Config.__configfile, encoding='UTF-8-sig')
        self.__testcasefile = config.get('TestCaseFile', 'file')
        self.__testcasejsonfile = config.get('TestCaseFile', 'jsonfile')
        self.__testcaseyamlfile = config.get('TestCaseFile', 'yamlfile')  
        self.__testApiKey = config.get('ApiKey', 'x-gaia-api-key') 
        self.__testUserName = config.get('LoginInfo', 'username') 
        self.__testUserPassword = config.get('LoginInfo', 'password')  
        self.__testUserUrl = config.get('LoginInfo', 'url') 
        self.__testUserApiType = config.get('LoginInfo', 'apiType')         
        self.__logpath = config.get('LogPath', 'path')
        self.__testUatUrl = config.get('Url', 'uat_url')
        self.__testSitUrl= config.get('Url', 'sit_url')
        self.__testProUrl = config.get('Url', 'pro_url')
        self.__test201 = config.get('Long_value', 'long_value_201')   
        self.__test501 = config.get('Long_value', 'long_value_501') 
        Config.__flag = True

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls.__instance_lock.acquire()
            if not hasattr(cls, '_instance'):
                cls._instance = super().__new__(cls)
            cls.__instance_lock.release()

        return cls._instance

    @property
    def testCaseJsonFile(self):
        return self.__testcasejsonfile

    @property
    def testCaseFile(self):
        return self.__testcasefile

    @property
    def logPath(self):
        return self.__logpath

    @property
    def testCaseYamlFile(self):
        return self.__testcaseyamlfile
    
    @property
    def testApiKey(self):
        return self.__testApiKey
    
    @property
    def testLoginName(self):
        return self.__testUserName

    @property
    def testLoginPassword(self):
        return self.__testUserPassword

    @property
    def testLoginUrl(self):
        return self.__testUserUrl
    
    @property
    def testLoginApiType(self):
        return self.__testUserApiType


    @property
    def testUatUrl(self):
        return self.__testUatUrl

    @property
    def testSitUrl(self):
        return self.__testSitUrl    

    @property
    def testProUrl(self):
        return self.__testProUrl 
    
    @property
    def test201(self):
        return self.__test201    

    @property
    def test501(self):
        return self.__test501  

if __name__ == '__main__':
    s1 =Config()
    s2 =s1.test501
    print('-----------------')
    print(s2,len(s2))
    
    

