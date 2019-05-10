import requests
url = "http://172.40.50.127:8888/login"
data = {'username':'abc','password':'abc'}
r = requests.post(url,data=data)
print(r.text)

r = requests.get("http://www.goubanjia.com")
print(r)