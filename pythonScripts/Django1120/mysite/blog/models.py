from django.db import models
import django.utils.timezone as timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    content = models.TextField()
    author = models.CharField(max_length=50)
    add_date = models.DateTimeField('添加日期', default=timezone.now)
    mod_date = models.DateTimeField('最后修改日期', auto_now=True)

#    def __str__(self):
#        return self.title
#
#
#class Comments(models.Model):
#    post = models.ForeignKey(Post, on_delete=models.CASCADE)
#    content = models.TextField(max_length=500)
#
#    def __str__(self):
#        return self.content
#
