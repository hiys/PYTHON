import urllib.request
import urllib.parse
url='http://www.goubanjia.com'
header = {
    'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0"
}
request = urllib.request.Request(url,headers=header)
response = urllib.request.urlopen(request).read()

fh = open('1.html','wb')
fh.write(response)
fh.close()