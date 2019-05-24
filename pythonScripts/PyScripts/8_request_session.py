import requests

url = "http://172.40.50.127:8888/login"
# 172.43.9.228:8888/login 上海IP
data = {'username':'abc','password':'abc'}
s = requests.Session()
s.post(url,data=data)
r = s.get("http://172.40.50.127:8888/")
print(r.text)