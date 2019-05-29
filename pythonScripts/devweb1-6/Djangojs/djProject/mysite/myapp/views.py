'''
[root@V1 mysite]# cat   -n   myapp/models.py
     1  from django.db import models
     2  from  django.utils import  timezone
     3  from    datetime   import  timedelta
     4  
     5  # Create your models here.
     6  class  Message(models.Model):
     7    msg = models.CharField(max_length=240)
     8    publish_date = models.DateTimeField(auto_now_add=True)
     9    def  __str__(self):
    10      return  self.msg
'''
from django.shortcuts import (render,
HttpResponse, get_object_or_404, redirect)
from   .models  import  Message
# Create your views here.#为myapp应用主页编写视图函数
def  hello(request):
  return  HttpResponse('<h1>Myapp hello OK</h1>')

def  message(request):
  if  request.method == 'POST':
#<textarea  name="liuyan"  id=""  cols="50" rows="8">
    msg = request.POST.get('liuyan')
#    m = Message(msg=msg)  #每次刷新页面也会有提交重复数据,缺陷
#    m.save()
    #.get_or_create(msg=msg)可以避免刷新页面重复提交数据
    Message.objects.get_or_create(msg=msg)

  msgs = Message.objects.all()
  return  render(request, 'message.html', {'msgs': msgs})

def  home(request):
  return  render(request, 'home.html')

def  login(request):
 # <label>用户名: </label><input  type="text" name="username" /><br/>
 # <label>密码: </label><input type="password"  name="password"/><br/>
  username = request.POST.get('username')
  password = request.POST.get('password')
  if username == 'bob' and password == '1234':
    request.session['IS_LOGIN'] = True
    return  redirect('protected')
  return  redirect('home')

def  protected(request):

  is_login = request.session.get('IS_LOGIN', False)
  if  is_login:
    return render(request, 'protect.html')
  return  redirect('home')

def  moban(request):
  astr = 'hello  world'
  alist = ['zhangsan', 'lisi', 'wangwu', 'zhaoliu']
  number = 100
  adict = {'bob': 23, 'alice': 20}
  context = {'mystr': astr, 'mylist': alist, 'mynum': number, 'mydict': adict}
  return  render(request, 'moban.html', context)


