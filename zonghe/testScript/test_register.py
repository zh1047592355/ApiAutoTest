'''
注册的脚本
'''

#测试数据
import pytest

from zonghe.baw import Member, DbOp
from zonghe.caw import DataRead


@pytest.fixture(params=DataRead.read_yaml("data_case/register_fail.yaml"))
def fail_data(request):
    return request.param

@pytest.fixture(params=DataRead.read_yaml("data_case/register_pass.yaml"))
def pass_data(request):
    return request.param

#测试逻辑
def test_register_fail(fail_data,url,baserequest):

    print(f"测试数据：{fail_data}")
    r=Member.register(url,baserequest,fail_data['data'])
    print(r.text)
    assert r.json()['msg']==fail_data['expect']['msg']

    #assert r.json()['code']==fail_data['expect']['code']

def test_register_success(url,baserequest,pass_data,db):
    mobile=pass_data['data']['mobilephone']
    r=Member.register(url,baserequest,pass_data['data'])
    print(r.text)
    assert r.json()['msg']==pass_data['expect']['msg']
    a=DbOp.select_user(db,mobile)
    assert mobile in a[0]
    print(a[0])
    DbOp.delete_user(db,mobile)


