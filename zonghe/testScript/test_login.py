'''
登录接口测试脚本
'''
import pytest
from zonghe.caw import DataRead
from zonghe.baw.Member import register,login
from zonghe.baw.DbOp import delete_user


@pytest.fixture(params=DataRead.read_yaml("data_case/login_setup.yaml"),scope='module')
def setup_data(request):
    return request.param

@pytest.fixture(params=DataRead.read_yaml("data_case/login_data.yaml"))
def login_fail(request):
    return request.param

@pytest.fixture(scope='module')
def registers(setup_data,url,baserequest,db):
    #注册用户

    register(url,baserequest,setup_data['casedata'])
    mobile=setup_data['casedata']['mobilephone']
    print('1111')
    yield
    print("22222")
    #删除注册用户
    delete_user(db,mobile)

def test_login(registers,url,baserequest,login_fail):
    #下发登陆请求
    #检查结果
    r=login(url,baserequest,login_fail['casedata'])
    print(r.json)
