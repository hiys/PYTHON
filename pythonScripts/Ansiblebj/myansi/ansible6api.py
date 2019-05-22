#!/usr/bin/env python
# -*- coding:utf8 -*-
'''
定义源文件的编码方式，使用流行编辑器中的格式化方式
# -*- coding:utf8 -*-
# -*- coding:latin-1 -*-
# -*- coding: iso-8859-15 -*-
# -*- coding:ascii -*-
#coding:UTF-8
#coding=UTF-8

interpreter         美 [ɪnˈtɜːrprətər]  
      n.口译工作者;口译译员;演绎(音乐、戏剧中人物等)的人;解释程序
constant　　　　　　英 [ˈkɒnstənt]
　　　adj.连续发生的;不断的;重复的;不变的;固定的;恒定的
　　　n.常数;常量
[root@V1 myansi]# ll  /usr/bin/env
-rwxr-xr-x. 1 root root 28992 4月  11 2018 /usr/bin/env
[root@V1 myansi]# file    /usr/bin/env
/usr/bin/env: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.32, BuildID[sha1]=3ad3b112c9cd9ef2e9cfa228c7996aa8ee1eb9c6, stripped

[root@V1 myansi]# type  python
python 是 /usr/bin/python
[root@V1 myansi]# ll  /usr/bin/python
lrwxrwxrwx. 1 root root 7 1月  26 12:33 /usr/bin/python -> python2
[root@V1 myansi]# ll  /usr/bin/python2
lrwxrwxrwx. 1 root root 9 1月  26 12:33 /usr/bin/python2 -> python2.7
[root@V1 myansi]# ll  /usr/bin/python2.7
-rwxr-xr-x. 1 root root 7216 4月  11 2018 /usr/bin/python2.7

[root@V1 myansi]# ansible   --version
ansible 2.8.0
  config file = /root/myansi/ansible.cfg
  configured module search path = [u'/root/.ansible/plugins/modules', u'/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/lib/python2.7/site-packages/ansible
  executable location = /usr/bin/ansible
  python version = 2.7.5 (default, Apr 11 2018, 07:36:10) [GCC 4.8.5 20150623 (Red Hat 4.8.5-28)]
[root@V1 myansi]# python  --version
Python 2.7.5

Documentation
Ansible
2.8
Python API

https://docs.ansible.com/ansible/latest/dev_guide/developing_api.html?highlight=python%20api
此示例是一个简单的演示，演示如何最低限度地运行几个任务：
sample    英 [ˈsɑːmpl]
     n.(抽查的)样本，样品;(化验的)取样，样本，
example   英 [ɪɡˈzɑːmpl]
     n.实例;例证;例子;典型;范例;样品;


'''
import json
import shutil
from collections import namedtuple
#from ansible.module_utils.common.collections import ImmutableDict

#DataLoader用于解析yaml/json/ini格式的文件
from ansible.parsing.dataloader import DataLoader
#VariableManager分析ansible 用到的变量
from ansible.vars.manager import VariableManager
#InventoryManager 分析主机清单文件
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
#TaskQueueManager管理任务队列
from ansible.executor.task_queue_manager import TaskQueueManager
#CallbackBase
from ansible.plugins.callback import CallbackBase
#from ansible import context
#constants 存储ansible一些预定义常量
import ansible.constants as C

import   sys
sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

class ResultCallback(CallbackBase):
  """用于在结果出现时执行操作的回调插件示例
    如果要将所有结果收集到一个对象中，以便在执行结束时进行处理，
    请使用``json``回调插件或编写自己的自定义回调插件.
  """
  def v2_runner_on_ok(self, result, **kwargs):
    """打印结果的JSON表示形式
       此方法可以将结果存储在实例属性中，以便以后检索。
    """
    host = result._host
    print(json.dumps({host.name: result._result}, indent=4))
    print('--*--' * 10)
#由于API是为CLI构造的，因此它希望在上下文对象中始终设置某些选项。
#context.CLIARGS = ImmutableDict(connection='local',
#  module_path=['/to/mymodules'], forks=10, become=None,
#  become_method=None, become_user=None, check=False, diff=False)

##创建一个Options类型，列表里为属性，这里用来设置ansible执行时的参数，
#如ask_pass,sudo_user等等(namedtuple创建一个和tuple类似的对象，
#命名的元组，比普通元组多了一个功能，可以给每个元组元素起名，类似字典key键名
#命名元组对象拥有可以访问的属性)
Options = namedtuple('Options', 
  ['connection', 'module_path', 'forks', 'become',
   'become_method', 'become_user', 'check', 'diff']
)
options = Options(connection='local', module_path=['/to/mymodules'],
  forks=10, become=None, become_method=None,
  become_user=None, check=False, diff=False
)

# 初始化所需对象
loader = DataLoader()  # 负责查找和读取yaml、json和ini文件
passwords = dict(vault_pass='secret')

# 实例化resultcallback，以便在结果传入时处理它们。
# Ansible希望这是其主要的展示渠道之一。
results_callback = ResultCallback()
print(type(results_callback),'\n--------*******-------\n')
print(results_callback)

# 创建清单，使用作为源的主机配置文件路径，或使用逗号分隔的字符串作为主机
inventory = InventoryManager(loader=loader, sources='localhost,')

# 变量管理器负责合并所有不同的源，以便为您提供每个上下文中可用变量的统一视图。
variable_manager = VariableManager(loader=loader, inventory=inventory)

# 创建代表我们的游戏（包括任务）的数据结构，这基本上是我们的yaml加载程序在内部所做的。
play_source =  dict(
  name = "Ansible Play",
  hosts = 'localhost',
  gather_facts = 'no',
  tasks = [
    dict(action=dict(module='shell', args='ls'), register='shell_out'),
    dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
  ]
)
# 创建play　object，playbook objects使用。
# 加载而不是初始化或新方法，这也将从play_source中提供的信息自动创建任务对象。
play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

# 运行它-实例化任务队列管理器，它负责分叉和设置所有对象，以便在主机列表和任务上迭代。
tqm = None
try:
  tqm = TaskQueueManager(
    inventory=inventory,
    variable_manager=variable_manager,
    loader=loader,
    passwords=passwords,
    stdout_callback=results_callback,  # 使用我们的自定义回调，而不是打印到stdout的"默认"回调插件
  )
  result = tqm.run(play) # 一出戏最有趣的数据实际上是发送到回调的方法
finally:
  # 我们总是需要清理子程序和我们用来与他们沟通的结构.
  if tqm is not None:
    tqm.cleanup()
  # Remove ansible tmpdir
  shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)


if __name__ == "__main__":
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)
  returnObj = ResultCallback()
  print(type(returnObj),'\n---------------\n')
  print(returnObj)
  


