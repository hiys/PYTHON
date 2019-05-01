from django.shortcuts import render, HttpResponse
from  .models  import  Post

# Create your views here.

def  index(request):
  page = request.GET.get('page');
  listPost = Post.objects.all()
  return render(request, "index.html", {'lstPost': listPost})
def  indexx(request):
  return render(request, "index.html")
def  hanshu(request):
  return HttpResponse("中文页面.Django/mysite/blog/views.py---hanshu");

def  test(request):
  a = [0, 1, 2, 3, 4]
  b = 'hello world'
  return render(request,'t.html', {'a':a, 'b' : b})
