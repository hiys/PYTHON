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
    print("#查看远程服务器的 头部信息 ",weather.getheaders())
    print("#查看响应 url 地址 ", weather.geturl())

    with  open(fname, 'wb') as  fobj:
      while True:
        html = weather.read(1024)
        print('二进制编码',html)
        #二进制编码 b'{"weatherinfo":{"city":"\xe5\xb9\xbf\xe5\xb7\x9e","cityid":"101280101","temp":"26.6","WD":"\xe4\xb8\x9c\xe5\x8d\x97\xe9\xa3\x8e","WS":"\xe5\xb0\x8f\xe4\xba\x8e3\xe7\xba\xa7","SD":"83%","AP":"1001.4hPa","njd":"\xe6\x9a\x82\xe6\x97\xa0\xe5\xae\x9e\xe5\x86\xb5","WSE":"<3","time":"17:50","sm":"1.7","isRadar":"1","Radar":"JC_RADAR_AZ9200_JB"}}'

        dumpstr = json.dumps(html.decode('utf8')) ##对简单数据类型进行编码
        print('json对象dumps(): ', dumpstr)
        #json对象dumps():  "{\"weatherinfo\":{\"city\":\"\u5e7f\u5dde\",\"cityid\":\"101280101\",\"temp\":\"26.6\",\"WD\":\"\u4e1c\u5357\u98ce\",\"WS\":\"\u5c0f\u4e8e3\u7ea7\",\"SD\":\"83%\",\"AP\":\"1001.4hPa\",\"njd\":\"\u6682\u65e0\u5b9e\u51b5\",\"WSE\":\"<3\",\"time\":\"17:50\",\"sm\":\"1.7\",\"isRadar\":\"1\",\"Radar\":\"JC_RADAR_AZ9200_JB\"}}"

        loadsdict = json.loads(dumpstr) ##对编码后的json对象进行decode解码
        print('dict--json.loads(): ', loadsdict)
        #dict--json.loads():  {"weatherinfo":{"city":"广州","cityid":"101280101","temp":"26.6","WD":"东南风","WS":"小于3级","SD":"83%","AP":"1001.4hPa","njd":"暂无实况","WSE":"<3","time":"17:50","sm":"1.7","isRadar":"1","Radar":"JC_RADAR_AZ9200_JB"}}

        #二进制编码 b''
        #json对象dumps():  ""
        #dict--json.loads(): 
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

#[root@room9pc01 devopsday04]# cat   weathergz.html && echo
#{"weatherinfo":{"city":"广州","cityid":"101280101","temp":"26.6","WD":"东南风","WS":"小于3级","SD":"83%","AP":"1001.4hPa","njd":"暂无实况","WSE":"<3","time":"17:50","sm":"1.7","isRadar":"1","Radar":"JC_RADAR_AZ9200_JB"}}
#[root@room9pc01 devopsday04]# ll   weathergz.html 
#-rw-r--r-- 1 root root 232 5月   9 12:23 weathergz.html

