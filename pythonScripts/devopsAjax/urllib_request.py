#!/usr/bin/env  python3
#coding:UTF-8
"""#coding=UTF-8
[root@V0 ~]# ls   /usr/local/lib/python3.6/site-packages/
django                         pytz
Django-1.11.20-py3.6.egg-info  pytz-2019.1.dist-info
easy_install.py                README.txt
get_dictionary_tuple.py        setuptools
pip                            setuptools-39.0.1.dist-info
pip-19.0.3.dist-info           sqlalchemy
pkg_resources                  SQLAlchemy-1.3.3-py3.6.egg-info
__pycache__                    tornado
pymysql                        tornado-6.0.2-py3.6.egg-info
PyMySQL-0.9.3.dist-info
[root@V0 ~]# cat   /usr/local/lib/python3.6/site-packages/README.txt 
This directory exists so that 3rd party packages can be installed
here.  Read the source for site.py for more details.
此目录存在，因此可以在此处安装第三方软件包。
有关详细信息，请阅读site.py的源文件。
[root@V0 ~]# ls   /usr/local/lib/python3.6/  |wc -l
204

/usr/local/lib/python3.6/urllib/request.py 
 324 class Request:
 325 
 326     def __init__(self, url, data=None, headers={},
 327                  origin_req_host=None, unverifiable=False,
 328                  method=None):
 329         self.full_url = url
 330         self.headers = {}
 331         self.unredirected_hdrs = {}
 332         self._data = None
 333         self.data = data
 334         self._tunnel_host = None
 335         for key, value in headers.items():
 336             self.add_header(key, value)
 337         if origin_req_host is None:
 338             origin_req_host = request_host(self)
 339         self.origin_req_host = origin_req_host
 340         self.unverifiable = unverifiable
 341         if method:
 342             self.method = method
"""
import urllib.request
#import urllib.parse
import  sys
sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

url='http://www.goubanjia.com'
header = {
 'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
}
request = urllib.request.Request(url,headers=header)
response = urllib.request.urlopen(request).read()

fh = open('1.html','wb')
fh.write(response)
fh.close()

with open('./1.html','rb') as fobj:
  data = fobj.readlines()
  print(data,end='\n\n')
print(" = = = = = = = =\n")


if  __name__ == '__main__':
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)




