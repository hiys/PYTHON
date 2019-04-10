#!/usr/bin/env  python3
import  sys, subprocess, time, datetime

#from datetime import * # 从模板 datetime 中 导入 所有的类*

print('\033[31;47;1m__name__ is %s \
sys.argv is %s\033[0m' % (__name__,sys.argv))

localt = time.localtime()
print('Local time is %s type is %s\n' % (localt,type(localt)))

#将元组的时间格式转换成字符串格式的时间
print('\033[32;46;1mLocalTime is %s \033[0m' \
% time.strftime('%Y-%m-%d %H:%M:%S', localt))

start = time.time()

time.sleep(0.1)

end = time.time()
print(end - start,end=' --end-start\n')

print('\033[33;40;1m datetime now is %s\033[0m' \
%  datetime.datetime.now())

print(time.time())
print()
print(time.ctime(time.time()))
print()
print(time.ctime())
print()
print(time.localtime())
print()
print(time.asctime(time.localtime()))
print()
print(time.asctime())
print()
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
print()
print(time.strftime('%Y-%m-%d %X',time.localtime()))
print()
print(time.strptime('2018-01-01 14:05:36',"%Y-%m-%d %X"))
print()
print(time.strptime(time.strftime('%Y-%m-%d %X',time.localtime()) ,"%Y-%m-%d %X"))
print()
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
print()
print(time.time())


print(time.strftime("%Y-%m-%d"))
print()
print(time.strftime("%Y|%m|%d"))
print()
print(time.strftime("%X"))
print()
print(time.strftime("%x"))
print()
print(time.strftime("%Y-%m-%d %x"))
print()
print(time.strftime("%Y-%m-%d %a"))
print()
print(time.strftime("%Y-%m-%d %A"))
print()
print(time.strftime("%Y-%m-%d %b"))
print()
print(time.strftime("%Y-%m-%d %B"))
print()
print(time.strftime("%Y-%m-%d %c"))
print()
print(time.strftime("%c"))

print(time.strftime("%Y-%m-%d %I"))

print(time.strftime("%Y-%m-%d %H"))

print(time.strftime("%Y-%m-%d %S"))

print(time.strftime("%Y-%m-%d%t%S"))

print(time.strftime("%Y-%m-%d%t%S"))

print(time.strftime("%Y-%m-%d%t%S"))

print(time.strftime("%Y-%m-%d %F"))

print(time.strftime("%Y-%m-%d %T"))

print(time.strftime("%Y-%m-%d %R"))

print('-------------datetime--------------')

print(datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S'))
print()
print(datetime.datetime.today().strftime('%Y-%m-%d %T'))
print()
print(datetime.datetime.strptime('2009-06-16 10:33:44', '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %X'))
print()
print(datetime.datetime.strptime('2009-06-16 10:33:44', '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %T'))

print()
datetime.timedelta(365).total_seconds() # 一年包含的总秒数

dt = datetime.datetime.now()

print(dt + datetime.timedelta(3))# 3天后

print(dt + datetime.timedelta(-3)) # 3天前
print()
print(dt + datetime.timedelta(hours= 3)) # 3小时后
print()
print(dt + datetime.timedelta(hours= -3)) # 3小时前
print()
print(dt + datetime.timedelta(hours= 3, seconds= 30)) # 3小时30秒后 

dat = datetime.datetime.now()

print(dat)

days = datetime.timedelta(days= 100,hours= 5)

print(dat + days)
 
print(dat - days)



if __name__ == '__main__':
  print('\033[30;43;1m sys.argv[0]is %s\033[0m' % sys.argv[0])


