'''
Cookie：
http协议：无状态、无连接、媒体独立。
每个请求都是独立的。有一些接口登录后才能访问，需要使用Cookies验证用户是否登录。
account/dashboard 用户没有登录时，返回登录的页面。
account/dashboard 如果登录了，返回用户的详细信息。浏览器登录后，获取到的cookie直接放到自动化来用。
如果cookie失效或者换其他用户登录，就不能继续访问了。
'''
import requests

# 百格网站，有一些接口登录之后才能访问。
print("未登录时，返回的结果为：")
url = "https://www.bagevent.com/account/dashboard"
r = requests.get(url)
print(r.text)

# 用Fiddler抓到的包，将里面的头设置到这里
head = {
    "Cookie": '__auc=a58783b91762c8012e0d67b6960; Hm_lvt_1fc37bec18db735c69ebe77d923b3ab9=1607064360; MEIQIA_TRACK_ID=1lBJ4p71TG3qErqqF29zUkHE8lb; _ga=GA1.2.657306528.1607065042; _gid=GA1.2.244399657.1607065042; BAGSESSIONID=512e3b28-6285-4057-a3ac-fcfd34e5b7e3; JSESSIONID=553BEB64C4C269DB4DFB0B7D5D9B0E81; __asc=c699a0901762cba0888d87befef; MEIQIA_VISIT_ID=1lBQmXyMYPx3FAS7i5eqwo34O9S; _gat=1; Hm_lpvt_1fc37bec18db735c69ebe77d923b3ab9=1607068169; BAG_EVENT_TOKEN_=02de735f68204d51009e7edda78e58c13a3fcdd1; BAG_EVENT_CK_KEY_="2780487875@qq.com"; BAG_EVENT_CK_TOKEN_=2440f5d17af838308ba4b390db81af38'
}
print("登录后，返回的结果为：")
r = requests.get(url, headers=head)
print(r.text)
