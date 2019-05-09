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


#[root@room9pc01 devopsday04]# python3  requestshtml.py
#__name__ is __main__
#<Response [200]>
#<Response [200]>
#sys.argv is ['requestshtml.py']
#[root@room9pc01 devopsday04]# tail  -2  /var/log/httpd/access_log
#127.0.0.1 - - [09/May/2019:17:09:37 +0800] "GET /?username=centos7&password=1234 HTTP/1.1" 200 9818 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
#127.0.0.1 - - [09/May/2019:17:09:37 +0800] "POST /?username=centos88&password=12333 HTTP/1.1" 200 9818 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
#





if __name__ == "__main__":
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)


