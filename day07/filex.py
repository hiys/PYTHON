#!/usr/bin/env  python3

fileobj = open('filex.txt')
data = fileobj.read(7)
fileobj.close()
print(data,end= '')

print('*' * 10)
fobj = open('filex.txt')
for line in fobj:
 print(line,end='')
fobj.close()

print('#' * 10)

fobj2 = open('filex.txt')
for  r  in  range(2):
  print(fobj2.readline(),end = '')
fobj2.close()

fobj3 = open('hello.txt','w')
fobj3.write('hello\tboy\n')
fobj3.close()

src_frb = '/usr/bin/ls'
dst_fwb = '/tmp/newls'

src_frb_obj = open(src_frb,'rb')
dst_fwb_obj = open(dst_fwb,'wb')

booleanrun = True
while  booleanrun :
  frbdata = src_frb_obj.read(4096)
  if  frbdata ==  b'':
    booleanrun = False
  dst_fwb_obj.write(frbdata)
else:
  src_frb_obj.close()
  dst_fwb_obj.close()
  print('Normal closure-------')

