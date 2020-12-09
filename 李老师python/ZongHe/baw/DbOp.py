'''
操作数据库
'''
from ZongHe.caw import Mysql


# 比如后续版本优化，将数据库从mysql换成sqlite了，脚本层不用改动，只需改动这个方法即可。
def delete_user(db, mobile):
    '''
    根据手机号码删除注册用户
    :param db:  数据库信息，字典格式的
    :param mobile: 手机号码
    :return:
    '''
    conn = Mysql.connect(db)
    sql = f"delete from member where mobilephone={mobile}"
    Mysql.execute(conn, sql)
    Mysql.disconnect(conn)


def select_user(db, mobile):
    '''
    根据手机号码查询用户
    :param db:
    :param mobile:
    :return:
    '''
    conn = Mysql.connect(db)
    sql = f"select mobilephone from member where mobilephone={mobile}"
    r = Mysql.execute_query(conn, sql)
    Mysql.disconnect(conn)
    return r
