#!/usr/bin/env  python3
#coding:UTF-8
#! -*- coding:utf8 -*-
"""#coding=UTF-8
中国天气网城市代码
101010100=北京
............
101280101=广州 
101280102=番禺 
101280105=花都 
101280106=天河 
http://www.weather.com.cn/data/sk/101280101.html  #广州 
  实况天气获取:http://www.weather.com.cn/data/sk/城市代码.html
>>> import  requests
>>> params = {'wd': 'centos7'}
>>> rq = requests.get('http://www.baidu.com/s',params=params)
>>> type(rq)
<class 'requests.models.Response'>
>>> rq
<Response [200]>
>>>  
https://www.baidu.com/s?wd=centos7
[root@room9pc01 devopsday04]# > /var/log/httpd/access_log
[root@room9pc01 devopsday04]# ll  /var/log/httpd/access_log
-rw-r--r-- 1 root root 0 5月   9 16:34 /var/log/httpd/access_log

>>> import  requests
>>> rq =  requests.get('http://127.0.0.1/zidir/x2.jpg')
>>> rq
<Response [200]>

>>> rq.content   #用字节的方式访问请求响应体,尤其是非文本请求(如图片)
b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00`\............
1\x1fu\x04\'tY)\xa0\x17\x10\xff\xd9'
>>> 
>>> with  open('newx2.jpg', 'wb')  as  fobj:
...  fobj.write(rq.content)
... 
227704
>>> 
[root@room9pc01 html]# ll  newx2.jpg 
-rw-r--r-- 1 root root 227704 5月   9 17:42 newx2.jpg
[root@room9pc01 html]# eog   newx2.jpg
^C
>>> url = 'http://www.weather.com.cn/data/sk/101280101.html'
>>> header = {
...   'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
... }
>>> rq = requests.get(url, headers = header)
>>> rq
<Response [200]>
>>> rq.text
'{"weatherinfo":{"city":"å¹¿å·\x9e","cityid":"101280101","temp":"26.6","WD":"ä¸\x9cå\x8d\x97é£\x8e","WS":"å°\x8fäº\x8e3çº§","SD":"83%","AP":"1001.4hPa","njd":"æ\x9a\x82æ\x97\xa0å®\x9eå\x86µ","WSE":"<3","time":"17:50","sm":"1.7","isRadar":"1","Radar":"JC_RADAR_AZ9200_JB"}}'
>>> rq.encoding
'ISO-8859-1'
>>> 
>>> rq.encoding = 'utf8'

>>> rq.encoding
'utf8'
>>> rq.json()
{'weatherinfo': {'city': '广州', 'cityid': '101280101', 'temp': '26.6', 'WD': '东南风', 'WS': '小于3级', 'SD': '83%', 'AP': '1001.4hPa', 'njd': '暂无实况', 'WSE': '<3', 'time': '17:50', 'sm': '1.7', 'isRadar': '1', 'Radar': 'JC_RADAR_AZ9200_JB'}}
>>> 

>>> myurl = 'http://127.0.0.1/xx'
>>> header = {
...  'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
... }
>>> rq=requests.get(url=myurl,headers = header)
>>> rq.status_code
404
>>> 
>>> rq.status_code == requests.codes.not_found
True
>>> rq.status_code == requests.codes.OK
False
>>> 
>>> rq.raise_for_status()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python3.6/site-packages/requests/models.py", line 940, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 404 Client Error: Not Found for url: http://127.0.0.1/xx
>>> 

>>> rq.headers   #服务器响应头部
{'Date': 'Thu, 09 May 2019 10:15:14 GMT', 'Server': 'Apache/2.4.6 (CentOS)', 'Content-Length': '200', 'Keep-Alive': 'timeout=5, max=100', 'Connection': 'Keep-Alive', 'Content-Type': 'text/html; charset=iso-8859-1'}
>>> 
raise     英 [reɪz]   美 [reɪz]  
       v.提升;举起;提起;(使)直立，站立;增加，提高(数量、水平等)
       n.高地;上升;加薪

expire   英 [ɪkˈspaɪə(r)] 
    v.(因到期而)失效，终止;到期;届满


•  当前可使用的Cookie规范有两个版本:
Cookie版本0
和Cookie版本1

•  Cookie版本1是对Cookie版本0的扩展,
版本1可以和版本0互操作
但是Cookie版本0 的使用范围更广泛

•  版本0定义了Set-Cookie响应首部、Cookie请求首部
•  Set-Cookie响应首部,
其实就是服务端返回的
Cookie信息,
具体的语法如下:

Set-Cookie:key=value;expires=date;domain=domain;path=path;secure	
	
key/value:
在服务端可跟踪、可识别的用户信息

expires:
Cookie结束日期,
如果没指定会在用户退出浏览器时过期

domain:
告诉浏览器这个Cookie可以被发送到哪个域名,
如果没指定,
默认为产生Cookie的服务器主机名,
浏览器会存储很多不同网站的Cookie,
浏览器会根据domain的值
将Cookie发送到对应的域名下

path:
指定Cookie对哪些请求路径生效,
如果没指定,
默认为产生Cookie的URL路径

secure:在使用SSL安全连接时才发送Cookie,
若没设置secure,则没限制	

•  版本0定义了Set-Cookie响应首部、Cookie请求首部
•  Set-Cookie响应首部,
其实就是服务端返回的Cookie信息
具体的语法如下:
>>>r=requests.get('http://www.baidu.com')
>>>r.cookies
>>>r1= requests.get('http://www.baidu.com', cookies=r.cookies)

>>> myurl = 'http://www.baidu.com'
>>> header = {
...  'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
... }
>>> rq=requests.get(url=myurl,headers = header)
>>> rq.status_code
200
>>> 
>>> rq.cookies
<RequestsCookieJar[Cookie(version=0, name='H_PS_PSSID', value='2453_1431_21105_28775_28724_28963_28834_28584_26350', port=None, port_specified=False, domain='.baidu.com', domain_specified=True, domain_initial_dot=True, path='/', path_specified=True, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={}, rfc2109=False), Cookie(version=0, name='delPer', value='0', port=None, port_specified=False, domain='.baidu.com', domain_specified=True, domain_initial_dot=True, path='/', path_specified=True, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={}, rfc2109=False), Cookie(version=0, name='BDSVRTM', value='0', port=None, port_specified=False, domain='www.baidu.com', domain_specified=False, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={}, rfc2109=False), Cookie(version=0, name='BD_HOME', value='0', port=None, port_specified=False, domain='www.baidu.com', domain_specified=False, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={}, rfc2109=False)]>

>>> rq1 = requests.get(myurl, cookies=rq.cookies)

>>> rq1
<Response [200]>

>>> type(rq1)
<class 'requests.models.Response'>

>>> rq1.cookies
<RequestsCookieJar[Cookie(version=0, name='BDORZ', value='27315', port=None, port_specified=False, domain='.baidu.com', domain_specified=True, domain_initial_dot=True, path='/', path_specified=True, secure=False, expires=1557485999, discard=False, comment=None, comment_url=None, rest={}, rfc2109=False)]>

>>> type(rq1.cookies)
<class 'requests.cookies.RequestsCookieJar'>

>>> rq1.status_code
200
>>> 

"""
import  requests, sys
sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

#payload = {'wd': 'centos7'}
#rq = requests.get('http://www.baidu.com/s',params=payload)
##等价于访问https://www.baidu.com/s?wd=centos7
#print(rq)
##<Response [200]>

#  <form action="/zidir" method="post">
#   <input type="text"  name="username">姓名
#   <input name="password">密码
#   <button type="submit">提交submit</button>
#  </form>

header = {
    'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
  }
url = 'http://127.0.0.1/'
payload = {'username': 'centos7', 'password':'1234'}
rq = requests.get(url, headers = header, params = payload)
print(rq)


payload = {'username': 'centos88', 'password':'12333'}
myurl = 'http://127.0.0.1/'
header = {
 'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
}
datawd = {'username':'valuex', 'password':'22233'} #data用于表单提交数据
file = {'file':open('/root/devopsday04/imgx1.jpg','rb') }
rq = requests.post(url= myurl, data=datawd,params = payload, files = file, headers = header, cookies={})
print(rq)






if __name__ == "__main__":
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)


