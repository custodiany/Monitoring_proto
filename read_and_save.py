import json
import sqlite3
from datetime import datetime
import os
import redfish
import time
import json


#svr_list = ["o1fdp02", "o1sdp02"] #장비명 기록
#svr_urlpass = {"o1fdp02" : ['10.14.119.8', 'LT7BWPQX'], "o1sdp02" : ['10.14.119.6', '48805321']} #장비별 ilo주소, 비밀번호 기록

svr_list = ['o1sdp01', 'o1sdp02', 'o1sdp03', 'o1sdp04', 'o1fdp01', 'o1fdp02', 'o1fdp03', 'o1fdp04', 'o1drf01', 'o1drf02', 'o1drf03', 't1drf05', 'o1sdr01', 'o1sdr02', 'o1sdr03', 'o1sdr04', 'o1efs01', 'o1efs02', 'o1efs03', 'o1efs04', 'o1cs0a', 'o1cs0b', 'o1cs1a', 'o1cs1b', 'o1app01', 'o1app02', 'm1nms01', 'm1nms02', 'o1was01', 'o1was02', 'o1byp01', 't1tsv01', 'm1pms01', 'e1sim01', 'e1sdr05', 'e1efs05', 'e1drf04', 'e1fdp05', 'e1sdp05', 'e1cs2a']
svr_urlpass = {'o1sdp01': ['10.14.85.1', '11294153'], "o1sdp02" : ['10.14.119.6', '48805321'], 'o1sdp03': ['10.14.85.21', '27393712'], 'o1sdp04': ['10.14.85.17', '35818959'], 'o1fdp01': ['10.14.85.3', '79554904'], "o1fdp02" : ['10.14.119.8', 'LT7BWPQX'], 'o1fdp03': ['10.14.85.18', '45196578'], 'o1fdp04': ['10.14.85.19', '15237167'], 'o1drf01': ['10.14.85.6', '48762493'], 'o1drf02': ['10.14.85.7', '75416327'], 'o1drf03': ['10.14.85.20', '61808972'], 't1drf05': ['10.14.85.26', '34301147'], 'o1sdr01': ['10.14.85.12', '35685936'], 'o1sdr02': ['10.14.85.13', '60862251'], 'o1sdr03': ['10.14.85.16', '66231778'], 'o1sdr04': ['10.14.85.22', '99957769'], 'o1efs01': ['10.14.85.14', '99383045'], 'o1efs02': ['10.14.85.15', '53619420'], 'o1efs03': ['10.14.85.23', '81198214'], 'o1efs04': ['10.14.85.24', '32322448'], 'o1cs0a': ['10.14.85.8', '15870262'], 'o1cs0b': ['10.14.85.9', '63229852'], 'o1cs1a': ['10.14.85.10', '17685812'], 'o1cs1b': ['10.14.85.11', '79695844'], 'o1byp01': ['10.14.85.5', '51650039'], 't1tsv01': ['10.14.85.25', '68054015'], 'o1app01': ['10.14.85.37', '01964893'], 'o1app02': ['10.14.85.38', '69685661'], 'm1nms01': ['10.14.85.45', '17457115'], 'm1nms02': ['10.14.85.46', '59789501'], 'm1pms01': ['10.14.85.44', '92276670'], 'o1was01': ['10.14.85.40', '51916166'], 'o1was02': ['10.14.85.41', '63765944'], 'e1sim01' : ['10.14.85.31', '66326725'], 'e1sdr05' : ['10.14.85.32', '96440171'], 'e1efs05':['10.14.85.33', '32761374'], 'e1drf04' : ['10.14.85.30', '99808039'], 'e1fdp05' : ['10.14.85.28', '41908874'], 'e1sdp05' : ['10.14.85.27', '63735303'], 'e1cs2a' : ['10.14.85.29', '96517635']}

#운영용
#svr_list = ['o1sdp01', 'o1sdp02', 'o1sdp03', 'o1sdp04', 'o1fdp01', 'o1fdp02', 'o1fdp03', 'o1fdp04', 'o1drf01', 'o1drf02', 'o1drf03', 't1drf05', 'o1sdr01', 'o1sdr02', 'o1sdr03', 'o1sdr04', 'o1efs01', 'o1efs02', 'o1efs03', 'o1efs04', 'o1cs0a', 'o1cs0b', 'o1cs1a', 'o1cs1b', 'o1app01', 'o1app02', 'm1nms01', 'm1nms02', 'o1was01', 'o1was02', 'o1byp01', 't1tsv01', 'm1pms01']
#svr_urlpass = {'o1sdp01': ['10.14.85.1', 11294153], 'o1sdp02': ['10.14.85.2', 12932179], 'o1sdp03': ['10.14.85.21', 27393712], 'o1sdp04': ['10.14.85.17', 35818959], 'o1fdp01': ['10.14.85.3', 79554904], 'o1fdp02': ['10.14.85.4', 12700318], 'o1fdp03': ['10.14.85.18', 45196578], 'o1fdp04': ['10.14.85.19', 15237167], 'o1drf01': ['10.14.85.6', 48762493], 'o1drf02': ['10.14.85.7', 75416327], 'o1drf03': ['10.14.85.20', 61808972], 't1drf05': ['10.14.85.26', 34301147], 'o1sdr01': ['10.14.85.12', 35685936], 'o1sdr02': ['10.14.85.13', 60862251], 'o1sdr03': ['10.14.85.16', 66231778], 'o1sdr04': ['10.14.85.22', 99957769], // 여기까지 검증'o1efs01': ['10.14.85.14', 99383045], 'o1efs02': ['10.14.85.15', 53619420], 'o1efs03': ['10.14.85.23', 81198214], 'o1efs04': ['10.14.85.24', 32322448], 'o1cs0a': ['10.14.85.8', 15870262], 'o1cs0b': ['10.14.85.9', 63229852], 'o1cs1a': ['10.14.85.10', 17685812], 'o1cs1b': ['10.14.85.11', 79695844], 'o1byp01': ['10.14.85.5', 51650039], 't1tsv01': ['10.14.85.25', 68054015], 'o1app01': ['10.14.85.37', '01964893'], 'o1app02': ['10.14.85.38', 69685661], 'm1nms01': ['10.14.85.45', 17457115], 'm1nms02': ['10.14.85.46', 59789501], 'm1pms01': ['10.14.85.44', 92276670], 'o1was01': ['10.14.85.40', 51916166], 'o1was02': ['10.14.85.41', 63765944]}
#정보T&E용
# svr_list = ['e1sim01', 'e1sdr05', 'e1efs05', 'e1drf04', 'e1fdp05', 'e1sdp05', 'e1cs2a']
# svr_urlpass = {'e1sim01' : ['10.14.85.31', 66326725], 'e1sdr05' : ['10.14.85.32', 96440171], 'e1efs05':['10.14.85.33', 32761374], 'e1drf04' : ['10.14.85.30', 99808039], 'e1fdp05' : ['10.14.85.28', 41908874], 'e1sdp05' : ['10.14.85.27', 63735303], 'e1cs2a' : ['10.14.85.29', 96517635]}




#---------------------read from svr에서 저장한 json파일 읽어오기, dictionary로 만들기 시작--------------------------------

def read_from_server(server_list, server_urlpass):
    for i in range(0,len(server_list)):
        response = os.system("ping -c 1 " + server_urlpass[server_list[i]][0])
        if response == 0:
            REST_OBJ = redfish.redfish_client(base_url = "https://" + server_urlpass[server_list[i]][0], username = 'Administrator', password = server_urlpass[server_list[i]][1])
            REST_OBJ.login(auth = "session")
            RESPONSE = REST_OBJ.get("/redfish/v1/Chassis/1/Thermal/")
            #f = open("/home/sys_mon/project/%s_status.txt" % svr_list[i], "w")
            data = RESPONSE.dict
            json.dump(data, open("./json/%s_status.json" % server_list[i], 'w'))
            #f.close()
            REST_OBJ.logout()
            time.sleep(5)
        else : print(server_urlpass[server_list[i]][0] + " is not connected")

def save_db_svrname(server_list): #fan 정보 db에 저장
    conn = sqlite3.connect('db.sqlite3') # fan 관련 db에 접속, db기본명칭 main
    c = conn.cursor()
    read = c.execute("SELECT svr_name FROM sys_mon_device")
    exist_list = []
    for i in read:
        if i[0] not in exist_list:
            exist_list.append(i[0])
    for i in range(0, len(server_list)):
        if server_list[i] in exist_list:
            c.execute("UPDATE sys_mon_device SET svr_name = :svr_name WHERE id = :id", {"id" : i+1, "svr_name" : server_list[i]}) #db 자료기록
            conn.commit()
        else :
            c.execute("INSERT INTO sys_mon_device VALUES(:id, :svr_name, null)", {"id" : i+1, "svr_name" : server_list[i]}) #db 자료기록
            conn.commit()
    conn.close()

def save_db_fan(server_list):
    #fan 정보 받아오기 위한 서버 리스트 및 data_fan 딕셔너리(이중구조) 생성
    data_fan = {}
    conn = sqlite3.connect('db.sqlite3') # fan 관련 db에 접속, db기본명칭 main
    c = conn.cursor()
    for i in range(0, len(server_list)):
        if os.path.exists("./json/%s_status.json" % server_list[i]):
            data_all = json.load(open("./json/%s_status.json" % server_list[i])) #추후에는 전체 while True와 For문 돌려서 주기적으로 읽어오기.
            for j in range(0, len(data_all["Fans"])):
                if data_all["Fans"][j]["Status"]["State"] == "Absent":
                    data_fan[server_list[i]] = {"fan_name" : data_all["Fans"][j]["FanName"], "fan_status" : data_all["Fans"][j]["Status"]["State"], "fan_health" : 0, "device_id" : i+1, "created_time" : datetime.now()}
                    c.execute("INSERT INTO sys_mon_fan (fan_name, fan_status, fan_health, device_id,created_time) VALUES (:fan_name, :fan_status, :fan_health, :device_id, :created_time)", data_fan[server_list[i]]) #db 자료기록
                    conn.commit() # db 저장
                    #원하는 값은, dict["o1fdp02"] = {"id" : index, "fan_name" : "fan1", "fan_status" : "enalbe", "fan_health" : "ok", "device_id" : svr_list_index}
                else : 
                    data_fan[server_list[i]] = {"fan_name" : data_all["Fans"][j]["FanName"], "fan_status" : data_all["Fans"][j]["Status"]["State"], "fan_health" : data_all["Fans"][j]["Status"]["Health"], "device_id" : i+1, "created_time" : datetime.now()}
                    c.execute("INSERT INTO sys_mon_fan (fan_name, fan_status, fan_health, device_id,created_time) VALUES (:fan_name, :fan_status, :fan_health, :device_id, :created_time)", data_fan[server_list[i]]) #db 자료기록
                    conn.commit()
                    #출력되는 값은, dict["o1fdp02"] = {"id" : index, "fan_name" : "fan1", "fan_status" : "enalbe", "fan_health" : "ok", "device_id" : svr_list_index}
    conn.close() #db 접속 종료
    time.sleep(3600)


#---------------------read from svr에서 저장한 json파일 읽어오기, dictionary로 만들기 끝-------------------------------------------------------------------------------

if __name__ == "__main__":
    conn = sqlite3.connect('db.sqlite3') # fan 관련 db에 접속, db기본명칭 main
    c = conn.cursor()
    c.execute("DELETE FROM sys_mon_device")
    conn.commit()
    pid = os.fork()
    while True:
        if pid:
                try:
                    pass
                    print("saving data is started")
                    save_db_svrname(svr_list)
                    save_db_fan(svr_list)
                    print("saving data is ended")
                except:
                    pass
        else:
                try:
                    print("reading data is started")
                    read_from_server(svr_list, svr_urlpass)
                    time.sleep(3600)
                    print("reading data is ended")
                except:
                    pass