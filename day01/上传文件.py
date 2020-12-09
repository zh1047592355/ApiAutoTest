'''
接口的功能是上传文件，比如上传头像，附件等
'''

import requests
url="http://www.httpbin.org/post"
#将本地文件上传到服务器上
file="d:/abc.txt"
with open(file,'r') as f:
    #字典，上传的文件：文件相关参数组成的元组
    #txt/plain是文件的类型
    load={
        "file1":(file,f,"txt/plain")
    }
    r=requests.post(url,files=load)
    print(r.text)
#上传图片
file2="c:/test.png"
with open(file2,mode='rb')as f:
    load={
        #文件名：file-tuple
        #file-tuple 可以是二元组，三元组，四元组
        "file2":(file2,f,"image/png")
    }
    r=requests.post(url,files=load)
    print(r.text)
#可以一次上传多个文件，文本和图片一起上传

with open(file,'r') as f1:
    with open(file2,mode='rb')as f2:
        load={
            'file1':(file,f1),
            "file2":(file2,f2,"image/png")
        }
        r=requests.post(url,files=load)
        print(r.text)
