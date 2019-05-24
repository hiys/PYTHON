import requests
from pyquery import PyQuery as pq

url ="http://172.40.50.127:8000/blog/add"

s = requests.Session()
response = s.get(url)
doc =pq(response.text)
inputVal = doc('input[name="csrfmiddlewaretoken"]').val()
print(inputVal)
data = {'csrfmiddlewaretoken':inputVal,
        'title':'requests post title',
        'desc':'requests post desc',
        'author':'requests',
        'content':'content'}
s.post(url,data=data)
