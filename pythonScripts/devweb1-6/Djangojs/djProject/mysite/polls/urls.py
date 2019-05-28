"""
[root@V1 djProject]# ls  /root/djProject/mysite/
manage.py  mysite  polls
#django项目基础目录默认设置是manage.py文件所在的目录/root/djProject/mysite/
"""
from django.conf.urls import url
from  .  import   views   #相对路径导入模块
urlpatterns = [
  #使用index函数响应http://192.168.1.11:8800/polls/主页请求，
  #该url的名字(name)是index
  url(r'^$', views.index, name='index'),  #http://192.168.1.11:8800/polls/
  #(?P<question_id>\d+)表示把(\d+)这个分组的内容保存到变量question_id中，并且把变量question_id作为函数views.detail的参数
  url(r'(?P<question_id>\d+)/$', views.detail, name='detail'), #http://192.168.1.11:8800/polls/1/
  url(r'(?P<question_id>\d+)/result/$', views.result, name='result'), #http://192.168.1.11:8800/polls/3/result/
  url(r'(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
]

