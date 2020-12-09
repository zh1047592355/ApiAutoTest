'''
cookie:
http协议：无状态，无连接，媒体独立
每个请求独立的，有一些接口登录后才能访问，需要使用cookies验证用户是否登录
account/dashboard 用户没有登录时，返回的是登录页面链接
account/dashboard 如果登录了，返回用户的详细信息，浏览器登录后，获取到的cookie直接放到自动化使用
如果cookie失效或者其他用户登录，就不呢继续访问了
'''
import requests
print("未登录时，返回结果")
url="https://www.bagevent.com/account/dashboard"
r=requests.get(url)
print(r.text)

head={
    "Cookie":'MEIQIA_TRACK_ID=1l8RPHoFT6kVZ2zMc0SqZRxqpyK; __auc=226e611417627469647cedc2c13; _ga=GA1.2.308802512.1606976724; _gid=GA1.2.2125638752.1606976724; BAG_EVENT_TOKEN_=02de735f68204d51009e7edda78e58c13a3fcdd1; BAG_EVENT_CK_KEY_="2780487875@qq.com"; BAG_EVENT_CK_TOKEN_=2440f5d17af838308ba4b390db81af38; BAGSESSIONID=332345a8-a7a0-4a42-8d71-731591f67488; JSESSIONID=F14DCEC2786F3F424C84C2A631C46552; __asc=915a9d861762cbcd8b96a866e2c; Hm_lvt_1fc37bec18db735c69ebe77d923b3ab9=1606976705,1606977240,1606986487,1607068342; Hm_lpvt_1fc37bec18db735c69ebe77d923b3ab9=1607068342; MEIQIA_VISIT_ID=1lBR95OqSE8cptyitJyg00yZfBu'
}

r=requests.get(url,headers=head)
print(r.text)