from django.shortcuts import render, HttpResponse

# Create your views here.

def  index(request):
  page = request.GET.get('page');
  return render(request, "index.html")
def  indexx(request):
  return render(request, "index.html")
def  hanshu(request):
  return HttpResponse("中文页面.Django/mysite/blog/views.py---hanshu");

