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

def  download(url, fname):
  header = {
    'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
  }
  myrequest = request.Request(url,headers=header)
  try:
    xiangy = request.urlopen(myrequest, timeout = 1.5)
  except  urllib.error.URLError as  er:
    if hasattr(e,"code"):
      print('状态码 e.code = ', e.code)
    elif hasattr(e, "reason"):
      print("异常原因e.reason = ", e.reason)
  except  ConnectionResetError as ce:
    print('连接被对等方重置 ce= ', ce)
    
  else:  #不发生异常才执行的语句
    print(xiangy, type(xiangy),end='\n--- xiangy ---\n')
    print("#查看远程服务器的 头部信息 ",xiangy.getheaders())
    print("#查看响应 url 地址 ", xiangy.geturl())

    html = xiangy.read()
    loadsdict = json.loads(html) ##对编码后的json对象进行decode解码
    print('dict--json.loads(): ', loadsdict)

#    with  open(fname, 'wb') as  fobj:
#    with  open(fname, 'w') as  fobj:
#      while True:
#        html = xiangy.read(1024)
#        html = xiangy.read()
#        print('二进制编码',html)
#        dumpstr = json.dumps(html.decode('gb18030')) ##对简单数据类型进行编码
#        dumpstr = json.dumps(html) ##对简单数据类型进行编码
#        print('json对象dumps(): ', dumpstr)
#        loadsdict = json.loads(dumpstr) ##对编码后的json对象进行decode解码

#        if  not html:
#          break
#        fobj.write(html)

  finally:    #不管是否异常都会执行的finally 语句
    xiangy.close() #关闭对象方法
    print("#查看响应状态信息 ", xiangy.getcode())


print('============= download(url, fname) ===================\n')


if __name__ == "__main__":
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)

  url = 'http://www.weather.com.cn/data/sk/101280101.html'
  fname = '/root/devopsday04/weathergz.html'
  download(url, fname)

  print('=============  weathergz.html  ===================\n')

  url = 'http://www.weather.com.cn/data/cityinfo/101280101.html'
  fname = '/root/devopsday04/gzcityinfo.html'
  download(url, fname)

  print('============= gzcityinfo.html ===================\n')

  url = 'http://www.weather.com.cn/data/zs/101280101.html'
  fname = '/root/devopsday04/gzzs.html'
  download(url, fname)

  print('============= gzzs.html ===================\n')




