from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Post,Comments
from django.core.paginator import Paginator, EmptyPage
from django.http import Http404


# Create your views here.

def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)
    page = request.GET.get('page', 1)
    try:
        posts = paginator.page(page)
    except EmptyPage:  # 如果页码太大，没有相应的记录
        posts = paginator.page(paginator.num_pages)  # 取最后一页的记录
    return render(request, "index.html", {'posts': posts})


# @login_required(login_url="/blog/login")
def showList(request):
    posts = Post.objects.all()

    return render(request, "list.html", {'posts': posts})


def add(request):
    if request.method == "POST":
        post = Post()
        post.title = request.POST.get('title')
        post.desc = request.POST.get('desc')
        post.content = request.POST.get('content')
        post.save()
        return HttpResponseRedirect("/blog/list")
    else:
        return render(request, "edit.html", {'action': "/blog/add/"})


def edit(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        post.title = request.POST.get('title')
        post.desc = request.POST.get('desc')
        post.content = request.POST.get('content')
        post.save()
        return HttpResponseRedirect("/blog/list")
    else:
        return render(request, "edit.html", {'action': "/blog/edit/{0}".format(id), 'post': post})


def detail(request, id):
    post = Post.objects.get(id=id)
    if post:
        return render(request, "detail.html", {'post': post})
    else:
        raise Http404


def delPost(request):
    post = Post.objects.get(id=request.GET.get("id"))
    post.delete()
    return HttpResponseRedirect("/blog/list")


def ajaxDel(request):
    post = Post.objects.get(id=request.GET.get("id"))
    post.delete()
    return JsonResponse({"code": 0, "msg": "删除成功"})


def loginView(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/blog/list')
        else:
            return HttpResponseRedirect('/blog/login')


def addComment(request):
    c = Comments()
    c.content = "abc"
    c.post_id = 1
    c.save()
    return HttpResponseRedirect("/blog/list")