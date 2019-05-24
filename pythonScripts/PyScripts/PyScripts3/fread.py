# 文件操作的三个步骤：打开、读写、关闭
# cp /etc/passwd mima

fobj = open('mima')   # 默认认为它是文本文件，以读的方式打开
data = fobj.read()    # 默认读取全部内容，也可以指定读取的字节数，如4096
fobj.close()
# print(data)

# --------------------------------
fobj = open('mima')
print(fobj.readline(), end='')  # 读取一行数据
print(fobj.readline(), end='')
print(fobj.readlines())    # 读取全部数据放到列表中
fobj.close()
# --------------------------------

fobj = open('mima')
for line in fobj:
    print(line, end='')
fobj.close()
