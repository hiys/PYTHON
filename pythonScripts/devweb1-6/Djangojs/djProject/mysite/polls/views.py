from django.shortcuts import (render, HttpResponse, 
get_object_or_404, redirect)
from   .models   import   Question, Choice

# Create your views here.
#request形参必须提供，表示用户的请求http://192.168.1.11:8800/polls/
#def   index(request):
#  return  HttpResponse('<h1>Polls OK</h1>')

#为polls主页编写视图函数
def   index(request):
  questions = Question.objects.all()
#>>> from    polls.models   import  (Question, Choice)
#>>> Question.objects.all()
#<QuerySet [<Question: 第一次创业，期待结果是什么？>, <Question: 业余爱好是哪些？>, <Question: 开源思想是指哪些？>, <Question: 中秋节日几号>, <Question: 上海明天气温预测?>, <Question: 什么时候收货利润?>]>

  return  render(request, 'polls/index.html', {'questions': questions})
  #向用户返回一个网页(模板),{'questions': questions}字典是传给网页的数据

def   detail(request, question_id):
#  question = Question.objects.get(id= question_id)
  question = get_object_or_404(Question, id=question_id)
  return  render(request, 'polls/detail.html', {'question': question})

def   result(request, question_id):
  question = get_object_or_404(Question, id=question_id)
  return  render(request, 'polls/result.html', {'question': question})

def   vote(request, question_id):
  choice_id = request.POST.get('c_id')
  c = get_object_or_404(Choice, id=choice_id)
  c.votes += 1
  c.save()
  return  redirect('result', question_id=question_id)

