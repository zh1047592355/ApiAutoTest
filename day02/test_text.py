import pytest
import requests

@pytest.fixture(params=[[{"mobilephone":"13213577531","pwd":'123456'},"手机号码已被注册"],
                        [{"mobilephone":"1321357753","pwd":'123456'},"手机号码格式不正确"],
                        [{"mobilephone":"111222333411","pwd":'123456'},"手机号码格式不正确"],
                        [{ "mobilephone":"1321357753-","pwd":'123456'},"手机号码格式不正确"],
                        [{ "mobilephone":"13z21357753","pwd":'123456'},"手机号码格式不正确"],
                        [{"mobilephone":"13213577531","pwd":'12345'},"密码长度必须为6~18"],
                        [{"mobilephone":"13213577531","pwd":'1234561234561234561'},"密码长度必须为6~18"],
                        [{"mobilephone":"","pwd":'123456'},"手机号不能为空"]])

                        #[{"mobilephone":"18721344799","pwd":'123456123456123456'},"注册成功"]])
def zhuce_data(request):
    return request.param
def test_01(zhuce_data):
    print(zhuce_data[0])
    print(zhuce_data[1])

def test_zhuce(zhuce_data):
    url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
    r=requests.get(url,params=zhuce_data[0])
    r=r.json()
    assert r['msg']==zhuce_data[1]
    print(r['msg'])


