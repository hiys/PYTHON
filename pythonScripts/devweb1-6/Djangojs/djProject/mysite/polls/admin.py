from django.contrib import admin
from    .models   import  Question, Choice

class  QuestionAdmin(admin.ModelAdmin):
  list_display = ('publish_date', 'question_text')
  list_filter = ('publish_date',)    #增加过滤器
  date_hierarchy = 'publish_date'    ##添加时间轴
  search_fields = ('question_text',)  #增加搜索功能
  ordering = ('-publish_date', 'question_text')
  #设置默认时间第一降序排列(注意'-publish_date'负号),question_text字段第二的排序规则

class  ChoiceAdmin(admin.ModelAdmin):
  list_display = ('question', 'choice_text', 'votes')
  raw_id_fields = ('question',)
  #添加Choice时，弹出页面显示的Question详情(必须是外键)
  #注意数据库django的表polls_choice 的外键question_id字段
  #question = models.ForeignKey(Question, on_delete=models.CASCADE)


# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)

