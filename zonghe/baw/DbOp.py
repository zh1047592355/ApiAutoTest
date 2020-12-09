'''
操作数据库
'''
from zonghe.caw import Mysql
#数据库从mysql换成sqlList了，脚本层不用改动，只需要改动这个方法即可
def delete_user(db,mobile):
    '''
    根据手机号码删除注册用户
    :param db:
    :param mobile:
    :return:
    '''
    conn = Mysql.connect(db)
    sql = "delete from member where mobilephone=%s" % mobile
    Mysql.dxecute(conn, sql)

    Mysql.disconnect(conn)

def select_user(db,mobile):
    conn = Mysql.connect(db)
    sql = "select * from member where mobilephone=%s"%mobile
    shuju=Mysql.dxecute(conn, sql)
    Mysql.disconnect(conn)
    return shuju




