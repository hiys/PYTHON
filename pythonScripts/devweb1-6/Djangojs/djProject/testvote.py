#!/usr/bin/env  python3
# -*- coding:utf8 -*-
'''
[root@V1 djProject]# pwd
/root/djProject
[root@V1 djProject]# ls   mysite/polls/templates/polls/
detail.html  index.html  result.html

[root@V1 mysite]# cat   -n    polls/templates/polls/detail.html 

    14    <form action="{% url 'vote' question_id=question.id %}" method="post">
    15     <p>{{ queston.question_text }}</p>
    16     {%  for  c  in  question.choice_set.all %}
    17      <label>
    18       <input  type="radio" name="c_id"  value="{{ c.id  }}"/>{{ c.choice_text }}
    19      </label>
    20     {%  endfor %}
    21     <input  type="submit"   value="提交"/>
    22    </form>

[root@V1 djProject]# ls   mysite/polls/
admin.py  __init__.py  models.py    templates  urls.py
apps.py   migrations   __pycache__  tests.py   views.py

view-source:http://192.168.1.11:8800/polls/2/
  <form action="/polls/2/vote/" method="post">
   <p></p>
   
    <label>
     <input  type="radio" name="c_id"  value="2"/>听音乐
    </label>
   
    <label>
     <input  type="radio" name="c_id"  value="4"/>看玄幻小说
    </label>
   
    <label>
     <input  type="radio" name="c_id"  value="5"/>旅游看海
    </label>
   
   <input  type="submit"   value="提交"/>
  </form>

http://192.168.1.11:8800/polls/2/result/
 业余爱好是哪些？
听音乐  得票数:0
看玄幻小说  得票数:0
旅游看海    得票数:3
>>> import   requests
>>> data = { 'c_id': '5'}
>>> requests.post("http://192.168.1.11:8800/polls/5/vote/", data=data)
<Response [200]>

[root@V1 mysite]# mysql  -uroot  -p123  -D django -e "
select *  from  polls_choice;"
+----+----------------------------+-------+-------------+
| id | choice_text                | votes | question_id |
+----+----------------------------+-------+-------------+
|  1 | 15000以上                  |     0 |           1 |
|  2 | 听音乐                     |     0 |           2 |
|  3 | 培养出20个专业人才         |     2 |           1 |
|  4 | 看玄幻小说                 |     0 |           2 |
|  5 | 旅游看海                   |     4 |           2 |
|  6 | 两年内投资回本             |     1 |           1 |
|  7 | 吃月饼                     |     0 |           4 |
|  8 | 19                         |     0 |           5 |
|  9 | 25                         |     3 |           5 |
+----+----------------------------+-------+-------------+
http://192.168.1.11:8800/polls/2/result/
业余爱好是哪些？
听音乐  得票数:0
看玄幻小说  得票数:0
旅游看海    得票数:4

--------result --------
[root@V1 djProject]# vim    testvote.py
'''
import   sys, requests
sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

url = "http://192.168.1.11:8800/polls/5/vote/"
data = { 'c_id': '5'}

for i  in range(10):
  requests.post(url, data=data)




if __name__ == "__main__":
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)

#[root@V1 djProject]# pyflakes   testvote.py
#[root@V1 djProject]# python3   testvote.py
#__name__ is __main__
#sys.argv is ['testvote.py']
#[root@V1 djProject]# mysql  -uroot  -p123  -D django -e "
#> select *  from  polls_choice;"
#+----+----------------------------+-------+-------------+
#| id | choice_text                | votes | question_id |
#+----+----------------------------+-------+-------------+
#|  1 | 15000以上                  |     0 |           1 |
#|  2 | 听音乐                     |     0 |           2 |
#|  3 | 培养出20个专业人才         |     2 |           1 |
#|  4 | 看玄幻小说                 |     0 |           2 |
#|  5 | 旅游看海                   |    14 |           2 |
#|  6 | 两年内投资回本             |     1 |           1 |
#|  7 | 吃月饼                     |     0 |           4 |
#|  8 | 19                         |     0 |           5 |
#|  9 | 25                         |     3 |           5 |
#+----+----------------------------+-------+-------------+
#http://192.168.1.11:8800/polls/2/result/
#业余爱好是哪些？
#听音乐  得票数:0
#看玄幻小说  得票数:0
#旅游看海    得票数:14
#
#--------result --------
#


