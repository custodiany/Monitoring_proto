import os
import redfish
import time
import json
svr_list = ["o1fdp02"] #장비명 기록
svr_urlpass = {"o1fdp02" : ['https://10.14.119.8', 'LT7BWPQX']} #장비별 ilo주소, 비밀번호 기록

#운영망
#svr_list = ["o1sdp01", "o1sdp02", "o1sdp03", "o1sdp04", "o1fdp01", "o1fdp02", "o1fdp03", "o1fdp04", "o1drf01", "o1drf02", "o1drf03", "t1drf05", "o1sdr01", "o1sdr02", "o1sdr03", "o1sdr04", "o1efs01", "o1efs02", "o1efs03", "o1efs04", "o1cs0a", "o1cs0b", "o1cs1a", "o1cs1b", "o1byp01", "t1tsv01", "o1app01", "o1app02", "m1nms01", "m1nms02", "m1pms01", "o1was01", "o1was02" ]
#svr_urlpass = {"o1sdp01" : ['https://]}
#------------------------------------1시간 주기로 각 장비당 5초간격, Thermal data 받아와 json으로 저장하기 시작----------------------------------------------

#while True:
for i in range(0,len(svr_list)):
    REST_OBJ = redfish.redfish_client(base_url = svr_urlpass[svr_list[i]][0], username = 'Administrator', password = svr_urlpass[svr_list[i]][1])
    REST_OBJ.login(auth = "session")
    RESPONSE = REST_OBJ.get("/redfish/v1/Chassis/1/Thermal/#Fans/")
    #f = open("/home/sys_mon/project/%s_status.txt" % svr_list[i], "w")
    data = RESPONSE.dict
    json.dump(data, open("./json/%s_status.json" % svr_list[i], 'w'))
    #f.close()
    REST_OBJ.logout()
    time.sleep(5)
 #   time.sleep(3600)

#------------------------------------1시간 주기로 각 장비당 5초간격, Thermal data 받아와 json으로 저장하기 끝----------------------------------------------