import sqlite3

#创建一个连接对象，连接到本地数据库
conn=sqlite3.connect("meeting.db")
#创建一个游标对象，调用其execute（）方法来执行SQL语句
c=conn.cursor()


#查询会议室表中的数据
sql_meeting="SELECT * FROM MEETINGROOM ORDER BY roomNo"

c.execute(sql_meeting)

ret = c.execute(sql_meeting).fetchone()



print(c.fetchone()[0])

for row in c.execute(sql_meeting):
    print(row)
    print(row[0]+row[1])


