"""site196 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^add/$',add),
    url(r'^list/$',showList),
    url(r'^edit/(?P<id>\d+)$',edit),
    url(r'^detail/(?P<id>\d+)$',detail,name="post_detail"),
    url(r'^del$',delPost),
    url(r'^addcomments$',addComment),
    url(r'^login', loginView)
]
