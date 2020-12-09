'''
pytest 是一种测试框架，用来方便的组织测试脚本，生成测试报告，或者与其他工具集成
命名要求：
1.测试文件以test_开头或者test结尾
2.测试类以Test开头
3.测试函数/方法以test_开头
执行
1.运行某个文件：pytest 脚本.py
2.运行某个文件中的用例：pytest 脚本.py::test_register_001
3.运行生成测试报告 pytest 脚本.py --html=report.html
4.多线程运行 pytest 脚本.py -n 3
5.失败重执行 pytest 脚本.py --reruns=3
'''
import requests
url="http://192.168.150.54:8089/futureloan/mvc/api/member/register"
def test_register_001():
    data={
        "mobilephone":"1321357753",
        "pwd":'123456'
    }
    r=requests.post(url,data=data)
    assert r.json()['msg']=="手机号码格式不正确"

def test_register_002():
    user = {
        "mobilephone": "13213577531",
        "pwd": '12345'
    }
    r = requests.get(url, params=user)
    r = r.json()
    assert r['msg'] == "密码长度必须为6~18"

def test_register_003():
    user = {
        "mobilephone": "13213577531",
        "pwd": '1234561234561234561'
    }
    r = requests.get(url, params=user)
    r = r.json()
    assert r['msg'] == "密码长度必须为6~18"

def test_register_004():
    user = {
        "mobilephone": "",
        "pwd": '123456'
    }
    r = requests.get(url, params=user)
    r = r.json()
    assert r['msg'] == "手机号不能为空"
