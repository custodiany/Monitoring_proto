import json
import sqlite3

conn = sqlite3.connect('db.sqlite3') # fan 관련 db에 접속, db기본명칭 main
c = conn.cursor() #커서 생성

#---------------------read from svr에서 저장한 json파일 읽어오기, dictionary로 만들기 시작--------------------------------

data_all = json.load(open("./json/o1fdp02_status.json")) #추후에는 전체 while True와 For문 돌려서 주기적으로 읽어오기.

#fan 정보 받아오기 위한 서버 리스트 및 data_fan 딕셔너리(이중구조) 생성
svr_list = ["o1fdp02"]
data_fan = {}


for i in range(0, len(svr_list)):
    data_all = json.load(open("./json/%s_status.json" % svr_list[i])) #추후에는 전체 while True와 For문 돌려서 주기적으로 읽어오기.



#Absent인 Fan에 대해서는 Health = 0, Enable인 Fan에 대해서는 Health='OK'
for i in range(0, len(svr_list)) : 
    for j in range(0, len(data_all["Fans"])):
        if data_all["Fans"][j]["Status"]["State"] == "Absent":
            data_fan[svr_list[i]] = {"fan_name" : data_all["Fans"][j]["FanName"], "fan_status" : data_all["Fans"][j]["Status"]["State"], "fan_health" : 0, "device_id" : i+1}
            c.execute("INSERT INTO sys_mon_fan (fan_name, fan_status, fan_health, device_id) VALUES (:fan_name, :fan_status, :fan_health, :device_id)", data_fan[svr_list[i]]) #db 자료기록
            conn.commit() # db 저장
            #원하는 값은, dict["o1fdp02"] = {"id" : index, "fan_name" : "fan1", "fan_status" : "enalbe", "fan_health" : "ok", "device_id" : svr_list_index}
        else : 
            data_fan[svr_list[i]] = {"fan_name" : data_all["Fans"][j]["FanName"], "fan_status" : data_all["Fans"][j]["Status"]["State"], "fan_health" : data_all["Fans"][j]["Status"]["Health"], "device_id" : i+1}
            c.execute("INSERT INTO sys_mon_fan (fan_name, fan_status, fan_health, device_id) VALUES (:fan_name, :fan_status, :fan_health, :device_id)", data_fan[svr_list[i]])
            conn.commit()
#출력되는 값은, dict["o1fdp02"] = {"id" : index, "fan_name" : "fan1", "fan_status" : "enalbe", "fan_health" : "ok", "device_id" : svr_list_index}

conn.close() #db 접속 종료


#---------------------read from svr에서 저장한 json파일 읽어오기, dictionary로 만들기 끝-------------------------------------------------------------------------------

