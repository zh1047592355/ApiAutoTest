'''
文件读写类的操作
'''
import configparser
import os

import yaml


def get_porject_path():
    '''
    获取工程路径
    :return: 当前工程路径，比如C:\ApiAutoTest\zonghe
    '''
    #__file__存储着当前文件的路径
    path=os.path.realpath(__file__)
    #上一级目录
    path=os.path.dirname(path)
    #在上一级目录
    path=os.path.dirname(path)
    return path+"\\"


def read_ini(file_path,key):
    '''
    读取ini配置文件
    :param file_path: 文件路径
    :param key: 要读取的key值
    :return: key对应的value
    '''
    file_path=get_porject_path()+file_path
    #print(file_path)
    config=configparser.ConfigParser()
    config.read(file_path)#读文件
    value=config.get("env",key)#通过key取value
    return value

def read_yaml(file_path):
    '''
    读取yaml文件
    :param file_path:yaml文件路径
    :return:文件内容，列表格式的
    '''
    file_path=get_porject_path()+file_path
    #print(file_path)
    with open(file_path,"r",encoding='utf-8')as f:
        content=yaml.load(f,Loader=yaml.FullLoader)
        return content

if __name__ == '__main__':
    #绝对路径，把代码放到别的电脑上，可能就执行不了
    #把绝对路径换成相对路径，C:\ApiAutoTest\zonghe通过代码自动获取
    a=read_ini(r'data_env\env.ini','url')
    print(a)
    b=read_ini(r"data_env\env.ini",'db')

    print(b)
    a=read_yaml(r"data_case\register_fail.yaml")
    print(a)