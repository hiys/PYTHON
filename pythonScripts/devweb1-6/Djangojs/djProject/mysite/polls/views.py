from django.shortcuts import render, HttpResponse

# Create your views here.
#request形参必须提供，表示用户的请求
def   index(request):
  return  HttpResponse('<h1>Polls OK</h1>')

