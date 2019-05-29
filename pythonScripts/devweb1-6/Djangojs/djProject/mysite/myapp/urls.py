"""
[root@V1 djProject]# ls   mysite/
manage.py  myapp  mysite  polls
#django项目基础目录默认设置是manage.py文件所在的目录/root/djProject/mysite/
"""
from django.conf.urls import url
from  .  import   views   #相对路径导入模块
urlpatterns = [
  #使用hello函数响应http://192.168.1.11:8800/myapp/hello主页请求，
  #该url的名字(name)是hello
  url(r'^hello', views.hello, name='hello'),  #http://192.168.1.11:8800/myapp/hello
  url(r'^message/$', views.message, name='message'),
  url(r'^home/$', views.home, name='home'),
  url(r'^login/$', views.login, name='login'),
  url(r'^protected/$', views.protected, name='protected'),
  url(r'^moban/$', views.moban, name='moban'),
]

