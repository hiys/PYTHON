from django.conf.urls import url
from  .views  import  index, hanshu, indexx, test

urlpatterns = [
    url(r'^$', index),
    url(r'^indexx$', indexx),
    url(r'^indexxx', hanshu),
    url(r'^t', test),
]
