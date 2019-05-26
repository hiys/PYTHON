from django.db import models
#import django.utils.timezone as timezone

# Create your models here.
class  Question(models.Model):
  question_text = models.CharField(max_length=200)
  publish_date = models.DateTimeField('date  published')

  def  __str__(self):
    return  self.question_text

class  Choice(models.Model):
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)
  question = models.ForeignKey(Question, on_delete=models.CASCADE)

