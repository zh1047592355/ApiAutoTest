'''
数据库的操作
'''
import pymysql


def connect(db):
    host=db['host']
    port=db['port']
    user=db['user']
    pwd=db['pwd']
    name=db['name']
    try:
        conn=pymysql.connect(host=host,port=port,user=user,password=pwd,database=name,charset='utf8')
        print("连接数据库成功")
        return conn
    except Exception as e:
        print("连接数据库失败，异常信息为：%s"%e)

def disconnect(conn):
    try:
        conn.close()
        print("断开数据库连接成功")
    except Exception as e:
        print("断开数据库连接失败，异常信息为%s"%e)

def dxecute(conn,sql):
    '''
    执行sql语句
    :param conn: connect返回的对象
    :param sql: 要执行的sql语句
    :return:
    '''
    try:
        c=conn.cursor() #获取游标
        c.execute(sql) #使用游标执行sql语句

        conn.commit() #提交
        shuju=c.fetchall()
        c.close() #关闭游标
        print("执行sql语句成功")
        return shuju



    except Exception as e:
        print("执行sql语句失败，异常信息为%s"%e)




if __name__ == '__main__':
    db={"host":"192.168.150.54","port":3306,"name":"apple","user":"root","pwd":"123456"}
    #db={"host":"192.168.150.222","port":4406,"name":"future","user":"root","pwd":"123456"}
    conn=connect(db)
    mobile='13513577531'
    sql="delete from member where mobilephone=%s"%mobile
    dxecute(conn,sql)

    disconnect(conn)

