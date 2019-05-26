"""
[root@V1 djProject]# ls  /root/djProject/mysite/polls/
admin.py  __init__.py  models.py    tests.py  views.py
apps.py   migrations   __pycache__  urls.py
[root@V1 djProject]# ls  /root/djProject/mysite/
manage.py  mysite  polls
#django项目基础目录默认设置是manage.py文件所在的目录/root/djProject/mysite/
"""
from django.conf.urls import url
from  .  import   views   #相对路径导入模块
urlpatterns = [
  #使用index函数响应http://192.168.1.11/polls/主页请求，
  #该url的名字(name)是index
  url(r'^$', views.index, name='index')  #http://192.168.1.11/polls/
]
