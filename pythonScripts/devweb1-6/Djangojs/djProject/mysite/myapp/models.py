from django.db import models
from  django.utils import  timezone
from    datetime   import  timedelta

# Create your models here.
class  Message(models.Model):
  msg = models.CharField(max_length=240)
  publish_date = models.DateTimeField(auto_now_add=True)
  def  __str__(self):
    return  self.msg

