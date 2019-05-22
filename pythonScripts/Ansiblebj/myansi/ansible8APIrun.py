#!/usr/bin/env python
#! -*- coding:utf8 -*-
'''
[root@V1 myansi]# python  --version
Python 2.7.5

Documentation
Ansible
2.8
Python API
https://docs.ansible.com/ansible/latest/dev_guide/developing_api.html
https://docs.ansible.com/ansible/latest/dev_guide/developing_api.html?highlight=python%20api
此示例是一个简单的演示，演示如何最低限度地运行几个任务：

https://docs.ansible.com/ansible/devel/modules/setup_module.html
https://docs.ansible.com/ansible/devel/modules/
https://docs.ansible.com/ansible/devel/
安装，升级和配置
安装指南
配置Ansible
Ansible移植指南
Ansible 2.9移植指南
Ansible 2.8移植指南
Ansible 2.7移植指南
Ansible 2.6移植指南
https://docs.ansible.com/ansible/latest/index.html
https://www.ansible.com/resources/videos/quick-start-video?extIdCarryOver=true&sc_cid=701f2000001OH7YAAW

https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html

'''
#import json
import shutil
from ansible.module_utils.common.collections import ImmutableDict
#DataLoader用于解析yaml/json/ini格式的文件
from ansible.parsing.dataloader import DataLoader
#VariableManager分析ansible 用到的变量
from ansible.vars.manager import VariableManager
#InventoryManager 分析主机清单文件
from ansible.inventory.manager import InventoryManager

from ansible.playbook.play import Play
#TaskQueueManager管理任务队列
from ansible.executor.task_queue_manager import TaskQueueManager
#from ansible.plugins.callback import CallbackBase
from ansible import context
#constants 存储ansible一些预定义常量
import ansible.constants as C

import   sys
sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

#class ResultCallback(CallbackBase):
#  def v2_runner_on_ok(self, result, **kwargs):
#    """打印结果的JSON表示形式
#       此方法可以将结果存储在实例属性中，以便以后检索。
#    """
#    host = result._host
#    print(json.dumps({host.name: result._result}, indent=4))

context.CLIARGS = ImmutableDict(connection='smart',
  module_path=['/to/mymodules'], forks=10, become=None,
  become_method=None, become_user=None, check=False, diff=False
)

loader = DataLoader()  # 负责查找和读取yaml、json和ini文件

#设置无密码(例如存储加密，远程链接或提升权限等密码)登录
passwords = dict()

# 实例化resultcallback，以便在结果传入时处理它们。
# Ansible希望这是其主要的展示渠道之一。
#results_callback = ResultCallback()

# 创建清单，使用作为源的主机配置文件路径，或使用逗号分隔的字符串作为主机
#说明被管理的主机列表清单，可以把各个主机用逗号分开，
#也可以使用主机清单文件路径,将文件路径存入主机列表清单中
#inventory = InventoryManager(loader=loader, sources='localhost,')
inventory = InventoryManager(loader=loader, sources = ["/root/myansi/myhosts"])

# 变量管理器负责合并所有不同的源，以便为您提供每个上下文中可用变量的统一视图。
##DataLoader用于解析yaml/json/ini格式的文件
variable_manager = VariableManager(loader=loader, inventory=inventory)

# 创建代表我们的剧本(包括任务)的数据结构，这基本上是我们的yaml加载程序在内部所做的.
play_source =  dict(
  name = "Asb Play",   #在脚本执行输出内容中显示#python  xx.py\nPLAY [Asb Play]
  hosts = 'other',     #执行ansible管理命令的主机地址(在主机列表清单中查找)
  gather_facts = 'no',  #不收集主机信息
  tasks = [ #以下是执行的命令
#    dict(action=dict(module='shell', args='ls'), register='shell_out'),
    #卸载httpd软件
#    dict(action=dict(module='yum', args='name=httpd state=absent'), register='shell_out'),
#在hosts = 'other'对应的#grep  -nA1 "other" myhosts文件指定的主机上安装现有版本的httpd 软件
    dict(action=dict(module='yum', args='name=httpd state=present'), register='shell_out'),
#    dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
    dict(action=dict(module='debug', args=dict(msg='{{shell_out}}')))
  ]
)
# 创建play　object，playbook objects使用。
# 加载而不是初始化或新方法，这也将从play_source中提供的信息自动创建任务对象。
play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

# 运行它-实例化任务队列管理器，它负责分叉和设置所有对象，以便在主机列表和任务上迭代。
tqm = None
try:  #任务队列管理器tqm实例对象
  tqm = TaskQueueManager(
    inventory=inventory,
    variable_manager=variable_manager,
    loader=loader,
    passwords=passwords,
#    stdout_callback=results_callback,  #使用我的自定义回调，而非打印到stdout的"默认"回调插件
  )
  result = tqm.run(play) # 一出戏最有趣的数据实际上是发送到回调的方法
finally:
  # 我们总是需要清理子程序和我们用来与他们沟通的结构.
  if tqm is not None:
    tqm.cleanup()
  # Remove ansible tmpdir 把临时目录文件删除
  shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)


if __name__ == "__main__":
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)






