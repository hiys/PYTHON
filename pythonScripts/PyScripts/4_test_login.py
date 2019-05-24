import urllib.request
import urllib.parse
url='http://172.40.50.127:8888'
header = {
    'Cookie' : "csrftoken=4EGTEFQvW1f00JVTa4FsgI1vWDYg4xnQ; sessionid=ni2fvu8zxtzt5sqkwaksporumcu90224; uid=2|1:0|10:1527942835|3:uid|4:YWJj|d9063b2a749b9b9eb3b47e31b15b521fc95b72f300bd444f5b66d98c746d2ba9"
}
request = urllib.request.Request(url,headers=header)
response = urllib.request.urlopen(request).read()
print(response)