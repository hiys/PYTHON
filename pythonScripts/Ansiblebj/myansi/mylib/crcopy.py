#!/usr/bin/env  python
# -*- coding:utf8 -*-
"""
管道连接
•  使用了管道连接后,与远程主机只有一个连接,命令
通过数据流的方式发送执行

•  此模式与有些系统程序兼容不太好
•  配置方式:
401:pipelining = True

[root@V1 myansi]# sed  -i   "s/^#\(pipelining = \)False/\1True/;"  /etc/ansible/ansible.cfg

[root@V1 myansi]# grep  -n  ^pipelining  /etc/ansible/ansible.cfg 
401:pipelining = True   #能够使得执行效率提高

/usr/lib/python2.7/site-packages/ansible/module_utils/basic.py
模块库目录
•  可以使用 ANSIBLE_LIBRARY环境变量来指定模块的存放位置
•  也可以在playbook当前目录下创建library目录

[root@V1 myansi]# mkdir   mylib
[root@V1 myansi]# echo  $ANSIBLE_LIBRARY  #环境变量

[root@V1 myansi]# export   ANSIBLE_LIBRARY=$(pwd)/mylib
[root@V1 myansi]# echo  $ANSIBLE_LIBRARY
/root/myansi/mylib
[root@V1 myansi]# ls   /root/myansi/mylib/

[root@V1 myansi]# cd   /root/myansi/mylib/
[root@V1 mylib]# vim   crcopy.py

"""
import    shutil
from   ansible.module_utils.basic  import  AnsibleModule
#from   ansible.module_utils.basic  import  AnsibleModule
import   sys
sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

def main():
  module = AnsibleModule(
    argument_spec=dict(
      yuan=dict(required=True, type='str'),
      mubiao=dict(required=True, type='str')
    )
  )
  print(module)
  print(type(module))

  shutil.copy(module.params['yuan'], module.params['mubiao'])
  module.exit_json(changed=True)






if __name__ == "__main__":
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)
  main()


