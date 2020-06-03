import sqlite3

conn=sqlite3.connect("meeting.db")
cursor = conn.cursor()

def dateCheck(strYmd,strHm,endYmd,endHm,roomName):
    sql = """SELECT strreserveYmd,strreserveHm,endreserveYmd,
            endreserveHm FROM RESERVE LEFT JOIN
            MEETINGROOM ON RESERVE.roomNo =
            MEETINGROOM.roomNo WHERE roomName = roomName
            ORDER BY endreserveYmd DESC"""
    for row in cursor.execute(sql):
        if (row[2] < strYmd):
            continue
        else:
            strTime = row[0] + row[1]
            endTime = row[2] + row[3]
            newStrTime = strYmd + strHm
            newEndTime = endYmd + endHm
            if(strTime <= newStrTime and endTime > newEndTime):
                return 1
            else:
                if (strTime <= newStrTime and newStrTime < endTime):
                    return 1
                else:
                    if (strTime < newEndTime and newEndTime <= endTime):
                        return 1
                    else :
                        break
                
    return 0
                
                
def setMeetingRoom():
    sql_meeting="SELECT * FROM MEETINGROOM"
    cursor.execute(sql_meeting)
    meetingRoom = []
    for row in cursor.execute(sql_meeting):
        meetingRoom.append(row[0])
    return meetingRoom
    
def insertReserve(strYmd,strHm,endYmd,endHm,roomName):
    sql1 = "SELECT * FROM MEETINGROOM WHERE roomName = roomName"
    cursor.execute(sql1)
    roomNo = cursor.fetchone()[1]
    sql2 = "INSERT INTO RESERVE VALUES(?,?,?,?,?)"
    datas = [(roomNo,strYmd,strHm,endYmd,endHm)]
    cursor.executemany(sql2,datas)
    conn.commit()

    
def zeroPad(str):
    if len(str) < 2:
        str = "0" + str
    return str
    
    
