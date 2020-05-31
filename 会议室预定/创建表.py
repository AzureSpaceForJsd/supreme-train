import sqlite3
#创建一个连接对象，连接到本地数据库
conn=sqlite3.connect("meeting.db")
#创建一个游标对象，调用其execute（）方法来执行SQL语句
c=conn.cursor()

sqlroom = """CREATE TABLE MEETINGROOM
        (roomName VARCHAR(50) NOT NULL PRIMARY KEY,
        roomNo VARCHAR(10) NOT NULL,
        roomAddress VARCHAR(256));"""
#创建会议室表
c.execute(sqlroom)

sqlreserve = """CREATE TABLE RESERVE
        (roomNo VARCHAR(10) NOT NULL,
        strreserveYmd VARCHAR(8) NOT NULL,
        strreserveHm VARCHAR(4) NOT NULL,
        endreserveYmd VARCHAR(8) NOT NULL,
        endreserveHm VARCHAR(4) NOT NULL,
        PRIMARY KEY(strreserveYmd,strreserveHm));"""
#创建预约表
c.execute(sqlreserve)
#初始化会议室表插入初始数据
sqlinit = "INSERT INTO MEETINGROOM VALUES(?,?,?)"
#声明要插入的会议室数据
datas = [("第一会议室","neusoft001","F50520"),
         ("第二会议室","neusoft002","F50518")]

#插入会议室数据
c.executemany(sqlinit,datas)

conn.commit()
conn.close()
