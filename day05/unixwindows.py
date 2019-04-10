#!/usr/bin/env  python3
import	 sys, subprocess, random, string

print('\033[31;40;1m__name__  is %s  sys.argv is  %s\033[0m' \
% (__name__,sys.argv))


def  unixtowindows(fname):
  dst_fname = fname + '.txt'
#  src_fobj = open(fname)
#  dst_fobj = open(dst_fname, 'w')
#  for  line in src_fobj:
#    line = line.rstrip('\r\n')
#    dst_fobj.write(line)
#  src_fobj.close()
#  dst_fobj.close()

  with open(fname) as src_fobj: #src和dst文件打开的先后顺序没有区别
    with open(dst_fname,'w') as dst_fobj:
      for  line in  src_fobj:
        print('old line---%s---' % line)
        line = line.rstrip('\r\n') + '\r\n'
  #先把旧的字符串靠右边的所有'\r\n'符号删除,再添加'\r\n'符号
        print('NEW LINE----%s----' % line)
        dst_fobj.write(line)
  

if __name__ == '__main__':

  print('\033[30;43;1m sys.argv[0]  is %s \033[0m' % sys.argv[0])
  unixtowindows(sys.argv[1])


