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
https://www.ansible.com/resources
https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html
https://docs.ansible.com/ansible/latest/reference_appendices/config.html
https://docs.ansible.com/ansible/latest/modules/tower_job_template_module.html


'''
#import json
#import shutil
from ansible.module_utils.common.collections import ImmutableDict
#DataLoader用于解析yaml/json/ini格式的文件
from ansible.parsing.dataloader import DataLoader
#VariableManager分析ansible 用到的变量
from ansible.vars.manager import VariableManager
#InventoryManager 分析主机清单文件
from ansible.inventory.manager import InventoryManager

#from ansible.playbook.play import Play
#TaskQueueManager管理任务队列
#from ansible.executor.task_queue_manager import TaskQueueManager
#from ansible.plugins.callback import CallbackBase
from ansible import context
#constants 存储ansible一些预定义常量
#import ansible.constants as C
from ansible.executor.playbook_executor import PlaybookExecutor

import   sys
sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

#class ResultCallback(CallbackBase):
#  def v2_runner_on_ok(self, result, **kwargs):
#    """打印结果的JSON表示形式
#       此方法可以将结果存储在实例属性中，以便以后检索。
#    """
#    host = result._host
#    print(json.dumps({host.name: result._result}, indent=4))

context.CLIARGS = ImmutableDict(connection='smart', sudo=None,
  remote_user=None, ask_pass=None, sudo_user=None, ask_sudo_pass=False,
  module_path=None, forks=5, become=None, verbosity=5,
  become_method=None, become_user=None, check=False, diff=False,
  listhosts=None, listtasks=None, listtags=None, syntax=None
)

print(context.CLIARGS)
#ImmutableDict({'listhosts': None, 'ask_pass': None, 'listtags': None, 'become_user': None, 'sudo': None, 'syntax': None, 'module_path': None, 'diff': False, 'check': False, 'ask_sudo_pass': False, 'remote_user': None, 'become_method': None, 'listtasks': None, 'verbosity': 5, 'connection': 'smart', 'become': None, 'forks': 5, 'sudo_user': None})

print(type(context.CLIARGS))
#<class 'ansible.module_utils.common.collections.ImmutableDict'>

loader = DataLoader()  # 负责查找和读取yaml、json和ini文件
print(loader)
#<ansible.parsing.dataloader.DataLoader object at 0x7f884894ec90>

print(type(loader))
#<class 'ansible.parsing.dataloader.DataLoader'>

#设置无密码(例如存储加密，远程链接或提升权限等密码)登录
passwords = dict()

# 实例化resultcallback，以便在结果传入时处理它们。
# Ansible希望这是其主要的展示渠道之一。
#results_callback = ResultCallback()

# 创建清单，使用作为源的主机配置文件路径，或使用逗号分隔的字符串作为主机
#说明被管理的主机列表清单，可以把各个主机用逗号分开，
#也可以使用主机清单文件路径/root/myansi/myhosts,将文件路径存入主机列表清单中
#inventory = InventoryManager(loader=loader, sources='localhost,')
#loader = DataLoader() 前面有定义负责查找和读取yaml、json和ini文件
inventory = InventoryManager(
  loader=loader, sources = ["/root/myansi/myhosts"]
)

print(inventory)
#<ansible.inventory.manager.InventoryManager object at 0x7f8848302090>

print(type(inventory))
#<class 'ansible.inventory.manager.InventoryManager'>


# 变量管理器负责合并所有不同的源，以便为您提供每个上下文中可用变量的统一视图。
##DataLoader用于解析yaml/json/ini格式的文件
variable_manager = VariableManager(
  loader=loader, inventory=inventory
)

print(variable_manager)
#<ansible.vars.manager.VariableManager object at 0x7f88482c0210>

print(type(variable_manager))
#<class 'ansible.vars.manager.VariableManager'>

def  run_pbook(pb_path):
  playbook = PlaybookExecutor(
    playbooks=pb_path,
    inventory=inventory,
    variable_manager=variable_manager,
    loader=loader,
    passwords=passwords
  )
  print(playbook)
  #<ansible.executor.playbook_executor.PlaybookExecutor object at 0x7f8848330890>

  print(type(playbook))
  #<class 'ansible.executor.playbook_executor.PlaybookExecutor'>
  result = playbook.run()
  print(result)

  print(type(result))
  return result




if __name__ == "__main__":
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)

  run_pbook(pb_path=['lamp.yml'])
  print('\nEND ---***--- PLAY OVER')




