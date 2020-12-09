import requests  #导入包

#发送一个get请求，返回一个响应，将响应存到变量r中
r= requests.get("http://www.baidu.com")
print(r.text)
#list 获取用户列表http://192.168.150.54:8089/
url="http://192.168.150.54:8089/futureloan/mvc/api/member/list"
r=requests.get(url)#发送请求
print(r.json())
r=r.json()
assert r['status']==1#对结果进行检查
assert r['code']=='10001'
assert r['msg']=='获取用户列表成功'

url="http://192.168.150.54:8089/futureloan/mvc/api/member/register?mobilephone=13298766789&pwd=123456"
r=requests.get(url)
r=r.json()
print(r)
assert r['status']==0
assert r['code']=='20110'
assert r['msg']=='手机号码已被注册'

#get请求带参数，方式2使用params参数
url="http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user={"mobilephone":"13213577531",
      "pwd":"123456",
      "rename":"hello"}
r=requests.get(url,params=user)
r=r.json()
print(r)
assert r["status"]==0
assert r['code']=='20110'
assert r['msg']=="手机号码已被注册"

#
url="http://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel=18521521219"
#phone={"tel":"18521531219"}
r=requests.get(url)
#r=requests.get(url,params=phone)
print(r.status_code)#状态码
print(r.reason)#状态信息
print(r.cookies)#cookies
print(r.encoding)#编码方式
print(r.headers)#响应头
r=r.text#文本信息
print(r)

#发送请求时，带请求头
#有些网址，对自动化发出去的请求不处理或处理的结果与实际的结果不一致
#通过设置请求头，伪装成浏览器发的请求
#httpbin是一个测试网址，发送的请求，这个网址将请求转成json格式的返回
url="http://www.httpbin.org/get?user=root&pwd=123123"
r=requests.get(url)
print(r.text)
#使用requests发送的请求，"User-Agent": "python-requests/2.24.0"
head={
    "user-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}
r=requests.get(url,headers=head)
print(r.text)

url="https://www.baidu.com/s?wd=lbj"
r=requests.get(url)
print(r.text)