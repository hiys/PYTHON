import os
import shutil
os.mkdir('/var/tmp/demo')  # 创建目录
os.listdir('/var/tmp/demo') # 列出目录内容
os.symlink('/etc/hosts', '/var/tmp/demo/zhuji') # 创建hosts的快捷方式
os.chdir('/var/tmp/demo')  # 切换目录
os.getcwd()  # 获得当前工作路径
shutil.copy('/etc/passwd', '.')  # 拷贝passwd到当前路径
os.curdir  # 当前工作路径
os.pardir  # 父目录
os.stat('passwd')  # passwd文件的属性
os.stat('passwd').st_size  # passwd文件的大小，以字节为单位
os.chmod('passwd', 0o600)  # 修改文件权限为600
os.mknod('abc.txt')  # 创建空文件abc.txt
os.remove('zhuji')  # 删除文件zhuji
os.path.abspath('abc.txt')  # abc.txt的绝对路径
os.path.basename('/var/tmp/demo/abc.txt')  # 返回abc.txt
os.path.dirname('/var/tmp/demo/abc.txt')  # 返回/var/tmp/demo
os.path.split('/var/tmp/demo/abc.txt')
os.path.join('/var/tmp/demo', 'abc.txt')  # 拼接路径
os.path.isfile('abc.txt') # 判断abc.txt存在并且是个文件
os.path.isdir('/etc')
os.path.exists('abc.txt')  # 存在abc.txt为True







