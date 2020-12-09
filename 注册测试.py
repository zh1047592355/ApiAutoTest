import requests

url="http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user={
    "mobilephone":"13213577531",
    "pwd":'123456'
}
r=requests.get(url,params=user)
r=r.json()
assert r['msg']=="手机号码已被注册"
print("测试1，手机已注册")


user={
    "mobilephone":"1321357753",
    "pwd":'123456'
}
r=requests.get(url,params=user)
r=r.json()
assert r['msg']=="手机号码格式不正确"
print("测试2，手机号码短")

user={
    "mobilephone":"111222333411",
    "pwd":'123456'
}
r=requests.get(url,params=user)
r=r.json()
assert r['msg']=="手机号码格式不正确"
print("测试3，测试手机长")

user={
    "mobilephone":"1321357753-",
    "pwd":'123456'
}
r=requests.get(url,params=user)
r=r.json()
assert r['msg']=="手机号码格式不正确"
print("测试4，手机含非法字符")

user={
    "mobilephone":"13z21357753",
    "pwd":'123456'
}
r=requests.get(url,params=user)
r=r.json()
assert r['msg']=="手机号码格式不正确"
print("测试5，手机号含字母")

user={
    "mobilephone":"13213577531",
    "pwd":'12345'
}
r=requests.get(url,params=user)
r=r.json()
assert r['msg']=="密码长度必须为6~18"
print("测试6，密码短")

user={
    "mobilephone":"13213577531","pwd":'1234561234561234561'
}
r=requests.get(url,params=user)
r=r.json()
assert r['msg']=="密码长度必须为6~18"
print("测试7，密码过长")

user={
    "mobilephone":"","pwd":'123456'
}
r=requests.get(url,params=user)
r=r.json()
assert r['msg']=="手机号不能为空"
print("测试8，手机号空")

user={
    "mobilephone":"13213577531",
    "pwd":''
}
r=requests.get(url,params=user)
r=r.json()
assert r['msg']=="密码不能为空"
print("测试9，密码空")


'''user={
    "mobilephone":"17614564668",
    "pwd":'123456',
    "rename":"============================================="
}
r=requests.get(url,params=user)
r=r.json()
assert r['msg']=="注册成功"
print("测试10，密码长度6")'''


'''user={
    "mobilephone":"17814564568",
    "pwd":'123456'
}
r=requests.get(url,params=user)
r=r.json()
assert r['msg']=="注册成功"
print("测试11，密码长度6")'''

'''user={
    "mobilephone":"18721349799",
    "pwd":'123456123456123456'
}
r=requests.get(url,params=user)
r=r.json()
print(r)
assert r['msg']=="注册成功"
print("测试12，密码长度为18")'''





