from django.shortcuts import render, HttpResponse
from   .models   import   Question

# Create your views here.
#request形参必须提供，表示用户的请求http://192.168.1.11:8800/polls/
#def   index(request):
#  return  HttpResponse('<h1>Polls OK</h1>')

#为polls主页编写视图函数
def   index(request):
  questions = Question.objects.all()
  return  render(request, 'polls/index.html', {'questions': questions})
  #向用户返回一个网页(模板),{'questions': questions}字典是传给网页的数据

