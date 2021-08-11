import requests
import json
from api.common.business import Token
from api.common.data_factory import DeptData
class TestDept:
    def test_dept_add_success(self):
        headers = {'Authorization':Token().token()}
        # 写法1
        with requests.post(url='http://flash-admin.enilu.cn/prod-api/dept',
                           params={'simplename':DeptData.simplename(),
                                   'fullname':DeptData.simplename(),
                                   'num':DeptData.seqnum(),
                                   'pid':1},
                           headers=headers) as response:
            d = json.loads(response.text)
            assert d.get('code') == 20000
            assert d.get('msg') == '成功'

        # 写法2
        # with requests.post(url='http://flash-admin.enilu.cn/prod-api/dept'
        #                        '?simplename=战略部001&fullname=中国市场战略部001&num=1&pid=1',
        #                    headers=headers) as response:
        #     print(response.text)

if __name__ == '__main__':
    from mimesis import Numbers
    p = Numbers('zh')
    print(p.integer_number(1,5))
    # for item in p._data.items():
    #     print(item)
    # t  = TestDept()
    # t.test_dept_add()