fobj = open('hello.txt', 'w')  # 文件不存在，创建；文件存在，清空
fobj.write('hello world!\n')
fobj.flush()  # 立即将缓存中的数据写入到磁盘，不是必须的
fobj.writelines(['2nd line.\n', '3rd line.\n'])
fobj.close()
