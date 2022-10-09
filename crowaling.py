import requests
#from bs4 import BeautifulSoup

url = "https://10.14.119.6"
req = requests.get(url)

#txt = BeautifulSoup(req.text, "html.parser")
print(req.text)
#"o1sdp02" : ['', '48805321']