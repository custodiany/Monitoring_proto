import json

data_all = json.load(open("./json/o1fdp02_status.json"))

#    data_all = read_inform('o1fdp02')
data_fanname = [0,0,0,0,0,0]
data_fanstatus = [0,0,0,0,0,0]
data_fanhealth = [0,0,0,0,0,0]
svr_list = ["o1fdp02"]

for i in range(0, len(data_all["Fans"])):
    if data_all["Fans"][i]["Status"]["State"] == "Absent":
        data_fanname[i] = data_all["Fans"][i]["FanName"]
        data_fanstatus[i] = data_all["Fans"][i]["Status"]["State"]
    else : 
        data_fanname[i] = data_all["Fans"][i]["FanName"]
        data_fanstatus[i] = data_all["Fans"][i]["Status"]["State"]
        data_fanhealth[i] = data_all["Fans"][i]["Status"]["Health"]

#print(type(data_fanname))
data_pre = list(zip(data_fanstatus, data_fanhealth))

#print(data_pre)
data_fan = { x:y for x,y in zip(data_fanname, data_pre)}
print(type(data_fan))
print(data_fan)