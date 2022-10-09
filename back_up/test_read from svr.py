import sys
import redfish
import time
import json
svr_list = ["o1fdp02"]
svr_urlpass = {"o1fdp02" : ['https://10.14.119.8', '96409143']}

#------------------------------------1시간 주기로 각 장비당 5초간격, Thermal data 받아와 json으로 저장하기 시작----------------------------------------------

#while True:
for i in range(0,len(svr_list)):
    REST_OBJ = redfish.redfish_client(base_url = svr_urlpass[svr_list[i]][0], username = 'Administrator', password = svr_urlpass[svr_list[i]][1])
    REST_OBJ.login(auth = "session")
    RESPONSE = REST_OBJ.get("/redfish/v1/Chassis/1/Thermal/")
    #f = open("/home/sys_mon/project/%s_status.txt" % svr_list[i], "w")
    data = RESPONSE.dict
    json.dump(data, open("./json/%s_status.json" % svr_list[i], 'w'))
    #f.close()
    REST_OBJ.logout()
    time.sleep(5)
 #   time.sleep(3600)

#------------------------------------1시간 주기로 각 장비당 5초간격, Thermal data 받아와 json으로 저장하기 끝----------------------------------------------