import pymysql
from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template
import json
# 创建链接
conn = pymysql.connect(
# 赋值给 conn连接对象
    host='127.0.0.1', # 本地回环地址
    port=3306,  # 默认端口
    user='root',  # 用户名
    password='123456789',  # 密码
    database='xyHotel', #连接的数据库名，也可以后续通过cursor.execture('user test_db')指定
    charset='utf8',  # 编码 不能写utf-8
    autocommit=True
)

# cursor = conn.cursor()
# cursor.execute('insert into userdata(hotelimageId,hotelname,personname,price,personphone,persontime) values("%s","%s","%s","%s", "%s", "%s");' % ('乔布斯', "2019","2019","2019","2019","2019"))
# conn.commit()

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

# cursor = conn.cursor()
# cursor .execute("create database xyHotel character set utf8;")
# # 执行完之后别忘了关闭游标和数据库连接
# cursor.close()
# conn.close()

# cursor = conn.cursor() # 创建一个游标
# sql = """
#     create table UserData(
#         id int auto_increment primary key ,
#         hotelimageId VARCHAR(255),
#         hotelname VARCHAR(255),
#         personname VARCHAR(255),
#         price VARCHAR(255),
#         personphone VARCHAR(255),
#         persontime VARCHAR(255)
#     );
# """
# cursor.execute(sql)
# cursor.close()
# conn.close()

@app.route('/QueryHotelData')
def QueryHotelData_view():
    # 生成一个游标对象(相当于cmd打开mysql中的 mysql>)
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 让数据自动组织成字典
    # 定义SQL语句
    sql = 'select * from hoteldata'
    # 执行SQL语句
    cursor.execute(sql)
    # 获取返回结果
    res = cursor.fetchall()
    return jsonify(res)

@app.route('/QueryRoomData')
def QueryRoomData_view():
    # 生成一个游标对象(相当于cmd打开mysql中的 mysql>)
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 让数据自动组织成字典
    # 定义SQL语句
    sql = 'select * from roomdata'
    # 执行SQL语句
    cursor.execute(sql)
    # 获取返回结果
    res = cursor.fetchall()
    return jsonify(res)

@app.route('/QueryUserData')
def QueryUserData_view():
    # 生成一个游标对象(相当于cmd打开mysql中的 mysql>)
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 让数据自动组织成字典
    # 定义SQL语句
    sql = 'select * from userdata'
    # 执行SQL语句
    cursor.execute(sql)
    # 获取返回结果
    res = cursor.fetchall()
    return jsonify(res)

@app.route('/PutUserData',methods=['POST', 'GET'])
def PutUserData_view():
    data = request.get_data()
    data2 = json.loads(data)    
    connect = pymysql.Connect(host='127.0.0.1', user='root', password='123456789', database='xyHotel')
    cursor = connect.cursor(cursor=pymysql.cursors.DictCursor)
    hotelimageId,hotelname,personname,personphone,persontime = data2['hotelimageId'],data2['hotelname'],data2['personname'],data2['personphone'],data2['persontime']
    sql = 'insert into userdata(hotelimageId,hotelname,personname,personphone,persontime) values(%(hotelimageId)s,%(hotelname)s,%(personname)s,%(personphone)s,%(persontime)s)'
    rows = cursor.execute(sql,{'hotelimageId': hotelimageId,'hotelname': hotelname,'personname': personname,'personphone': personphone,'persontime': persontime})
    # 这里一定要提交
    connect.commit()
    sql = 'select * from userdata'
    # 执行SQL语句
    cursor.execute(sql)
    # 获取返回结果
    res = cursor.fetchall()
    cursor.close()
    connect.close()
    return jsonify(res)

@app.route('/PutRoomData',methods=['POST', 'GET'])
def PutRoomData_view():
    data = request.get_data()
    data2 = json.loads(data)
    connect = pymysql.Connect(host='127.0.0.1', user='root', password='123456789', database='xyHotel')
    cursor = connect.cursor(cursor=pymysql.cursors.DictCursor)
    hotelimageId,hotelname,name, price,address,detail = data2['hotelimageId'],data2['hotelname'],data2['name'],data2['price'],data2['address'],data2['detail']
    sql = 'insert into roomdata(hotelimageId, hotelname,name, price,address,detail) values(%(hotelimageId)s,%(hotelname)s,%(name)s,%(price)s,%(address)s,%(detail)s)'
    rows = cursor.execute(sql,{'hotelimageId': hotelimageId,'hotelname': hotelname,  'name': name, 'price': price,'address': address,'detail': detail})
    # 这里一定要提交
    connect.commit()
    sql = 'select * from userdata'
    # 执行SQL语句
    cursor.execute(sql)
    # 获取返回结果
    res = cursor.fetchall()
    cursor.close()
    connect.close()
    return jsonify(res)

@app.route('/PutHotelData',methods=['POST', 'GET'])
def PutHotelData_view():
    data = request.get_data()
    data2 = json.loads(data)
    connect = pymysql.Connect(host='127.0.0.1', user='root', password='123456789', database='xyHotel')
    cursor = connect.cursor(cursor=pymysql.cursors.DictCursor)
    hotelimageId, name, price,address,detail = data2['hotelimageId'],data2['name'],data2['price'],data2['address'],data2['detail']
    sql = 'insert into hoteldata(hotelimageId, name, price,address,detail) values(%(hotelimageId)s,%(name)s,%(price)s,%(address)s,%(detail)s)'
    rows = cursor.execute(sql,{'hotelimageId': hotelimageId, 'name': name, 'price': price,'address': address,'detail': detail})
    # 这里一定要提交
    connect.commit()
    sql = 'select * from userdata'
    # 执行SQL语句
    cursor.execute(sql)
    # 获取返回结果
    res = cursor.fetchall()
    cursor.close()
    connect.close()
    return jsonify(res)

@app.route('/DeleteData',methods=['POST', 'GET'])
def DeleteHotelData_view():
    data = request.get_data()
    data2 = json.loads(data)
    connect = pymysql.Connect(host='127.0.0.1', user='root', password='123456789', database='xyHotel')
    cursor = connect.cursor(cursor=pymysql.cursors.DictCursor)
    hotelname = data2['hotelname']
    name = data2['name']
    if not(hotelname=="") and not(name==""):
        sql = 'delete from roomdata where name=%s'%name
        rows = cursor.execute(sql)
        # 这里一定要提交
        connect.commit()
    if not(hotelname=="") and name=="":
        sql = 'delete from roomdata where hotelname=%s'%hotelname
        rows = cursor.execute(sql)
        # 这里一定要提交
        connect.commit()
        sql = 'delete from hoteldata where name=%s'%hotelname
        rows = cursor.execute(sql)
        connect.commit()
    sql = 'select * from hoteldata'
    # 执行SQL语句
    cursor.execute(sql)
    # 获取返回结果
    res = cursor.fetchall()
    cursor.close()
    connect.close()
    return jsonify(res)

@app.route('/DeleteUserData',methods=['POST', 'GET'])
def DeleteUserData_view():
    data = request.get_data()
    data2 = json.loads(data)
    connect = pymysql.Connect(host='127.0.0.1', user='root', password='123456789', database='xyHotel')
    cursor = connect.cursor(cursor=pymysql.cursors.DictCursor)
    hotelname = data2['hotelname']
    persontime =data2['persontime']
    print(hotelname)
    print(persontime)
    sql = 'delete from userdata where hotelname=%s'%hotelname+ ' and persontime=%s'%persontime
    rows = cursor.execute(sql)
    # 这里一定要提交
    connect.commit()
    sql = 'select * from userdata'
    # 执行SQL语句
    cursor.execute(sql)
    # 获取返回结果
    res = cursor.fetchall()
    cursor.close()
    connect.close()
    return jsonify(res)

@app.route('/ModifyHotelData',methods=['POST', 'GET'])
def ModifyHotelData_view():
    connect = pymysql.Connect(host='127.0.0.1', user='root', password='123456789', database='xyHotel')
    cursor = connect.cursor(cursor=pymysql.cursors.DictCursor)
    hotelimageId, name, price,address,detail = input('hotelimageId, name, price,address,detail: ').split()
    sql = "update userinfo set detail=%s where name=%s"
    rows = cursor.executemany(sql, [(detail, name)])
    # 这里一定要提交
    cursor.commit()
    cursor.close()
    connect.close()

@app.route('/ModifyRoomData',methods=['POST', 'GET'])
def ModifyRoomData_view():
    connect = pymysql.Connect(host='127.0.0.1', user='root', password='123456789', database='xyHotel')
    cursor = connect.cursor(cursor=pymysql.cursors.DictCursor)
    hotelimageId, hotelname,name, price,address,detail = input('hotelimageId, hotelname,name, price,address,detail: ').split()
    sql = "update userinfo set detail=%s where name=%s"
    rows = cursor.executemany(sql, [(detail, name)])
    # 这里一定要提交
    cursor.commit()
    cursor.close()
    connect.close()

if __name__ == "__main__":
    # debug=True 代码修改能运行时生效，app.run运行服务
    # host默认127.0.0.1 端口默认5000
    app.run(host='127.0.0.1',port=5000,debug=True)
#    app.run(debug=True)
