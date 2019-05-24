import shutil

with open('/etc/hosts') as src_fobj:
    with open('/tmp/zhuji', 'w') as dst_fobj:
        shutil.copyfileobj(src_fobj, dst_fobj)
# cat /etc/hosts
# cat /tmp/zhuji

shutil.copyfile('/etc/hosts', '/tmp/zj')

# 将count.py的权限设置为与/usr/bin/ls一样，windows不支持
shutil.copymode('/usr/bin/ls', 'count.py')

# 将count2.py的状态设置为与count.py一样
# stat count.py 查看count.py的状态信息
shutil.copystat('count.py', 'count2.py')

# mkdir /tmp/demo
# 将/etc/hosts拷贝到/tmp/demo目录中
shutil.copy('/etc/hosts', '/tmp/demo')

# 相当于cp -p
shutil.copy2('/etc/login.defs', '/tmp/demo')

# 拷贝目录
shutil.copytree('/etc/security', '/tmp/demo/anquan')

# 删除目录
shutil.rmtree('/tmp/demo/anquan')

# 移动文件
shutil.move('/tmp/demo/hosts', '/var/tmp')

# 修改文件的属主属组都改为名是mail的用户
shutil.chown('/tmp/demo/login.defs', 'mail', 'mail')
