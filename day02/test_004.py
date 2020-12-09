'''
fixture 测试前置和后置
1.命名比较灵活，不限于setup，teardown等命名方式
2。使用灵活
3.不需要import即可实现共享
'''
import pytest
#测试前置
@pytest.fixture()#yield之前是前置
def login():
    print("登录系统")
    yield#yield之后是后置
    print("退出系统")

#测试脚本
def test_query():
    print("查询功能，不需要登录")
#使用方式一：将fixture作为参数传到脚本中
def test_add(login):
    print("添加功能，需要登录")
#方式二：使用注解
@pytest.mark.usefixtures("login")
def test_delete():
    print("删除功能，需要登录")