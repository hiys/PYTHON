#!/usr/bin/env   python3
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
101280201=韶关
http://www.weather.com.cn/data/sk/101280101.html  #广州 
  实况天气获取:http://www.weather.com.cn/data/sk/城市代码.html
 
"""
import   sys, json, urllib.error
from    urllib  import  request

sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

url = 'http://www.weather.com.cn/data/sk/101280101.html'
fname = '/root/devopsday04/weathergz.html'


def  download(url, fname):
  header = {
    'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
  }
  myrequest = request.Request(url,headers=header)
  try:
    weather = request.urlopen(myrequest, timeout = 1.5)
  except  urllib.error.URLError as  er:
    if hasattr(e,"code"):
      print('状态码 e.code = ', e.code)
    elif hasattr(e, "reason"):
      print("异常原因e.reason = ", e.reason)
  except  ConnectionResetError as ce:
    print('连接被对等方重置 ce= ', ce)
    
  else:  #不发生异常才执行的语句
    print(weather, type(weather),end='\n--- weather ---\n')
    #<http.client.HTTPResponse object at 0x7f384281ac18> <class 'http.client.HTTPResponse'>
    #--- weather --
    print("#查看远程服务器的 头部信息 ",weather.getheaders())
    ##查看远程服务器的 头部信息  [('Date', 'Thu, 09 May 2019 04:00:31 GMT'), ('Content-Type', 'text/html'), ('Transfer-Encoding', 'chunked'), ('Connection', 'close'), ('Server', 'nginx'), ('Age', '1514221'), ('X-Via', '1.1 jszjsx49:5 (Cdn Cache Server V2.0), 1.1 PSjsyzdx5rv60:8 (Cdn Cache Server V2.0), 1.1 PSgddgdx5kx62:7 (Cdn Cache Server V2.0)')]

    print("#查看响应 url 地址 ", weather.geturl())
    ##查看响应 url 地址  http://www.weather.com.cn/data/sk/101280101.html
    with  open(fname, 'wb') as  fobj:
      while True:
        html = weather.read(1024)
        print(json.dumps(html.decode('utf8')))  ##对简单数据类型进行编码
        #"{\"weatherinfo\":{\"city\":\"\u5e7f\u5dde\",\"cityid\":\"101280101\",\"temp\":\"26.6\",\"WD\":\"\u4e1c\u5357\u98ce\",\"WS\":\"\u5c0f\u4e8e3\u7ea7\",\"SD\":\"83%\",\"AP\":\"1001.4hPa\",\"njd\":\"\u6682\u65e0\u5b9e\u51b5\",\"WSE\":\"<3\",\"time\":\"17:50\",\"sm\":\"1.7\",\"isRadar\":\"1\",\"Radar\":\"JC_RADAR_AZ9200_JB\"}}"
        #""
        if  not html:
          break
        fobj.write(html)

  finally:    #不管是否异常都会执行的finally 语句
    weather.close() #关闭对象方法
    print("#查看响应状态信息 ", weather.getcode())
    ##查看响应状态信息  200
download(url, fname)

print('============= download(url, fname) ===================\n')


if __name__ == "__main__":
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)

#[root@room9pc01 devopsday04]# ll  weathergz.html 
#-rw-r--r-- 1 root root 232 5月   9 12:00 weathergz.html
#[root@room9pc01 devopsday04]# cat   weathergz.html
#{"weatherinfo":{"city":"广州","cityid":"101280101","temp":"26.6","WD":"东南风","WS":"小于3级","SD":"83%","AP":"1001.4hPa","njd":"暂无实况","WSE":"<3","time":"17:50","sm":"1.7","isRadar":"1","Radar":"JC_RADAR_AZ9200_JB"}}[root@room9pc01 devopsday04]# 
#




