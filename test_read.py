import sys
import json

data = json.load(open("json/o1fdp02_status.json"))
#print(len(data["Fans"]))
#print(data['Temperatures'][0]['ReadingCelsius'])

for i in data['Temperatures']:
    if i['Status']['State'] == 'Enabled' :
        print(i['Name'])
    else:
        pass