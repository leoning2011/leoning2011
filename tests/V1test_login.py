import requests
import json
import pytest
# data = [11,22,33,44] ,单个参数，单个数据
# data = [(11,22),(44,55),(77,88),(33,99)] # data的长度是测试用例数据的条数
data = [{'username':'','password':'','checkpoint':[{'code':9999},{'msg':'登录时失败'}]},
        # {'username':'huice','password':'','checkpoint':[{'code':9999}]},
        # {'username':'','password':'123','checkpoint':[{'code':9999},{'msg':'登录时失败'}]},
        # {'username':'huice','password':'123','checkpoint':[{'code':9999},{'msg':'登录时失败'}]}
        ]
#
# data = [[11,22],[44,55],[77,88],[33,99]]

# data：数据类型可以是元组，也可以是列表（默认）
class TestLogin:

    def test_login_success(self):
        with requests.post(url='http://flash-admin.enilu.cn/prod-api/account/login',
                                 headers={'Content-Type':'application/x-www-form-urlencoded'},
                                 data={'username':'developer','password':'developer'}) as response:
            # 服务器返回的数据：response.text，数据格式是json
            # python数据结构：字典、列表、元组、集合，没有json，所以需要转换
            # python操作json数据的方式，需要把json格式的数据转换成字典，通过操作字典完成对json数据的访问
            # json和python字典最明显的区别，json数据的key必须是双引号字符串，python字典的key可以是双引号，也可以是单引号
            # json转换成字典
            d = json.loads(response.text)
            assert response.status_code >= 200 and response.status_code < 400

            assert d.get('code') == 20000
            assert d.get('msg') == '成功'

    # 反向测试用例：
    # 1、用户名为空，密码为空；
    # 2、用户名长度小于5个字符，密码为空；
    # 3、用户名长度合法但不正确，密码合法
    # 4、用户名长度合法，密码长度为1

    # 期望结果：{"code":9999,"msg":"登录时失败","data":null,"success":false}

    # @pytest.mark.fail
    @pytest.mark.parametrize('user', data)
    def test_login_fail(self, user):
        url = 'http://flash-admin.enilu.cn/prod-api/account/login'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        userdata = {'username': user.get('username'), 'password': user.get('password')}

        with requests.post(url=url,
                           headers=headers,
                           data=userdata) as response:
            d = json.loads(response.text)
            checks = user.get('checkpoint')  #第一条用例数据：checks=[{'code':9999},{'msg':'登录时失败'}]

            # 执行检查
            for item in checks: # 遍历每个检查点
                # 第一次循环checks，item的值是：{'code':9999}
                # 第二次循环checks，item的值是：{'msg':'登录时失败'}

                # 第一种写法
                # for k in item.keys():   # 遍历该检查点的期望值
                #     assert d.get(k) == item.get(k)  # d.get(k)---实际值，item.get(k)---期望值

                # 第二种写法
                for k,v in item.items():  # 遍历该检查点的期望值
                    assert d.get(k) == v  # d.get(k)---实际值，v---期望值
            #
            # assert d.get('code') == checks[0].get('code')
            # assert d.get('msg') == checks[1].get('msg')

# # dd = [{'code':9999},{'msg':'登录时失败'}]
# d = {'code':9999}
# for k in d.keys():
#     print(k)

# if __name__ == '__main__':
#     login = TestLogin()
#     login.test_login_success()

# from 父 import 子
# 模块、函数、类的方法中

# 必须参数必须写在所有参数的最前面
# 定义参数时加*号表示传入的数据类型是元组
# 在使用时，加*号，去掉小括号（取值）
# y=9 默认值参数，可选参数

# 测试用例：输入数据、执行、验证（期望结果）
