import urllib.request
import urllib.parse
url = "http://172.40.50.127:8888/login"
# 172.43.9.228:8888/login 上海IP
data = {'username':'admin','password':'admin'}
postdata = urllib.parse.urlencode(data).encode('utf-8')
request = urllib.request.Request(url,data=postdata)
response = urllib.request.urlopen(request).read()
print(response)
response = urllib.request.urlopen("http://172.40.50.127:8888/").read()
print(response)