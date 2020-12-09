'''
member模块的接口
'''

def register(url,baserequest,data):
    '''
    注册接口
    :param url: 环境信息，比如http://jy001:8080/
    :param baserequest:BaseRquest的实例
    :param data: 注册的测试数据
    :return: 响应信息
    '''
    url=url+"futureloan/mvc/api/member/register"
    r=baserequest.post(url,data=data)
    return r

def login(url,baserequest,data):
    '''

    :param url:
    :param daserequest:
    :param data:
    :return:
    '''
    url=url+"futureloan/mvc/api/member/login"
    r=baserequest.post(url,data=data)
    return r
if __name__ == '__main__':
    from zonghe.caw.BaseRequests import BaseRequest
    b=BaseRequest()
    canshu={"mobilephone":"13213577531","pwd":'123456'}
    r=register("http://jy001:8081/",b,canshu)
    print(r.text)