import requests

url="http://192.168.150.54:8089/futureloan/mvc/api/member/login"
user={
    "mobilephone":'1321357751',
    "pwd":"123456"
}
r=requests.get(url,params=user)
r=r.json()
assert r["msg"]=="用户名或密码错误"
print("登录测试1，账号错")

user={
    "mobilephone":'13213577531',
    "pwd":"1234567"
}
r=requests.get(url,params=user)
r=r.json()
assert r["msg"]=="用户名或密码错误"
print("登录测试2，密码错")

user={
    "mobilephone":'',
    "pwd":"123456"
}
r=requests.get(url,params=user)
r=r.json()
assert r["msg"]=="手机号不能为空"
print("登录测试3，账号空")

user={
    "mobilephone":'13213577531',
    "pwd":""
}
r=requests.get(url,params=user)
r=r.json()
assert r["msg"]=="密码不能为空"
print("登录测试4，密码空")

user={
    "mobilephone":'13213577531',
    "pwd":"123456"
}
r=requests.get(url,params=user)
r=r.json()
assert r["msg"]=="登录成功"
print("登录测试5，正确登录")