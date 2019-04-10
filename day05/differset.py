#!/usr/bin/env  python3
import  sys, subprocess, random, string, getpass

print('\033[31;47;1m__name__  is %s  sys.argv is  %s\033[0m' \
% (__name__,sys.argv))

def   contrast():

#  src_fobj = open(fname)
#  dst_fobj = open(dst_fname, 'w')
#  for  line in src_fobj:
#    line = line.rstrip('\r\n')
#    dst_fobj.write(line)
#  src_fobj.close()
#  dst_fobj.close()

  with  open('./mima') as todaySrcObj:
    todset = set(todaySrcObj)
  with open('./passwd') as yesterdayObj:
    yeset = set(yesterdayObj)
  print('yesterdayset - todayset -- ./passwd  ----------------')
  print('\033[32;47;1m %s \033[0m' % (yeset - todset))
  print()
  print('todayset - yesterdayset --./mima ===============')
  print(todset - yeset)
  
  with open('/tmp/result.txt','w') as dstobj:
    dstobj.writelines(todset - yeset)
  
  print()
  with open('/tmp/result.txt','r') as  srcObj:
    print(srcObj.readlines())


if __name__ == '__main__':
  print('\033[30;43;1m sys.argv[0]  is %s \033[0m' % sys.argv[0])
  
  contrast()

