import json
import sqlite3
from datetime import datetime
import os
import redfish
import time
import json

svr_list = ["o1fdp02", "o1sdp02"] #장비명 기록
svr_urlpass = {"o1fdp02" : ['10.14.119.8', 'LT7BWPQX'], "o1sdp02" : ['10.14.119.6', '48805321']} #장비별 ilo주소, 비밀번호 기록



def read_from_server(server_list, server_urlpass):
    for i in range(0,len(server_list)):
        response = os.system("ping -c 1 " + server_urlpass[server_list[i]][0])
        if response == 0:
            REST_OBJ = redfish.redfish_client(base_url = "https://" + server_urlpass[server_list[i]][0], username = 'Administrator', password = server_urlpass[server_list[i]][1])
            REST_OBJ.login(auth = "session")
            RESPONSE = REST_OBJ.get('/redfish/v1/Chassis/1/Thermal/#Fans/')
            #f = open("/home/sys_mon/project/%s_status.txt" % svr_list[i], "w")
            data = RESPONSE.dict
            json.dump(data, open("./json/test/%s_chassis_thermal.json" % server_list[i], 'w'))
            #f.close()
            REST_OBJ.logout()
            time.sleep(5)
        else : print(server_urlpass[server_list[i]][0] + " is not connected")


#---------------------read from svr에서 저장한 json파일 읽어오기, dictionary로 만들기 끝-------------------------------------------------------------------------------

if __name__ == "__main__":
    try:
        print("reading data is started")
        read_from_server(svr_list, svr_urlpass)
        print("reading data is ended")
    except:
        pass