# 实现cp  /usr/bin/ls  /tmp/ls  这样的功能

src_fname = '/usr/bin/ls'
dst_fname = '/tmp/ls'

src_fobj = open(src_fname, 'rb')
dst_fobj = open(dst_fname, 'wb')

while True:
    data = src_fobj.read(4096)   # 每次读4096字节
    if data == b'':              # 读不到数据意味着读写完毕，中断循环
        break
    dst_fobj.write(data)         # 将数据写到目标文件

src_fobj.close()
dst_fobj.close()
