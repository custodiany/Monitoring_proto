import json

#print(type(svr_list))
#print(svr_list.index('o1sdp01'))
svr_list = ["o1fdp02"]
data_fan = {}
data_fanname = [0,0,0,0,0,0]
data_fanstatus = [0,0,0,0,0,0]
data_fanhealth = [0,0,0,0,0,0]

#원하는 값은, dict["o1sdp01"] = {"id" : index, "fan_name" : "fan1", "fan_status" : "enalbe", "fan_health" : "ok", "device_id" : svr_list_index}
for i in range(0, len(svr_list)):
    data_all = json.load(open("./json/%s_status.json" % svr_list[i])) #추후에는 전체 while True와 For문 돌려서 주기적으로 읽어오기.

#총 6개 Fan 관련해서 정보 받아오기 위한 리스트 생성



#Absent인 Fan에 대해서는 Health = 0, Enable인 Fan에 대해서는 Health='OK'
for i in range(0, len(svr_list)) : 
    for j in range(0, len(data_all["Fans"])):
        if data_all["Fans"][j]["Status"]["State"] == "Absent":
            data_fan[svr_list[i]] = {"id" : j, "fan_name" : data_all["Fans"][j]["FanName"], "fan_status" : data_all["Fans"][j]["Status"]["State"], "fan_health" : 0, "device_id" : i+1}
            #  해당 값 sqlite3 db에 저장
            print(data_fan)
        else : 
            data_fan[svr_list[i]] = {"id" : j, "fan_name" : data_all["Fans"][j]["FanName"], "fan_status" : data_all["Fans"][j]["Status"]["State"], "fan_health" : data_all["Fans"][j]["Status"]["Health"], "device_id" : i+1}
            print(data_fan)
        
# print(data_fan)