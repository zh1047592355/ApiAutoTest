'''
如果多个fixture带参数，参数之间是全组合的关系
'''
import pytest

@pytest.fixture(params=["root","admin","administrator"])
def user(request):
    return request.param

@pytest.fixture(params=["123456","888888","password","pwd_1234"])
def pwd(request):
    return request.param
#如果多个fixture带参数，参数之间是全组合的关系，3*4个测试数据
def test_login(user,pwd):
    print("用户名:%s,密码:%s"%(user,pwd))