#!/usr/bin/env  python3
import  sys, os, pickle, time, random
from  functools  import  reduce
from  functools  import  partial
import  tkinter    # tk-devel  tcl-devel 是模版tkinter依赖的软件包
import  sqlite3    # sqlite-devel sqlite #模版sqlite3 依赖的软件包 

"MoBan ------------ instruction"
print('\033[31;47;1m__name__  is %s\033[0m' %  __name__)

date = time.strftime('%Y年*%m月*%d日 %H时:%M分:%S秒',time.localtime())

#def  additive(x, y):  #[数]加法
#  return  x + y

#def  subtraction(x, y):  #减法
#  return  x - y

def  lambdaxy():

  zifulbiao = ['列表解析%d' % i**2 for i in range(1,8) if i >= 5 ] ##i 的2次方
  print(zifulbiao)
    #['列表解析25', '列表解析36', '列表解析49']

  cmds = { '+': lambda  x, y: x + y , '-': lambda  x, y: x - y }  #将#匿名函数存入字典
  nums = [ random.randint(2,10) for i in range(2) ] # 生成两个数
  nums.sort(reverse=True)  # 降序排列(从大 到小)

  op = random.choice('+-')  #自动随机选择加减法
  result = cmds[op](*nums)  # 调用存入字典的函数，把nums列表拆开，作为参数传入
  prompt = "%s %s %s = " % (nums[0], op, nums[1])
  print("正确的解答是 %s%s\n" % (prompt, result))
  #正确的解答是 10 - 6 = 4  # 注意每次的算法(加+ ,减法-)和数字都是随机的,不一样的

  abc = lambda x, y : x * y   #匿名函数
  print(type(abc))
    #<class 'function'>

  print('%d * %d =  %d' % (nums[0], nums[1], abc(nums[0],nums[1])))
   #10 * 6 =  60 #注意每次的数字都是随机的


def  filterfunlist():
  def  functionx1(x):
    return x % 2    #返回值 是 1 (True)  或 零 0 (False)

#-------------  #过滤出 列表 [10,11,22,30,7]  内部 的 所有 奇数 -----
# list( filter( 函数名functionx1 作为参数, 
 #   列表[10,11,22,30,7]中的每一个元素 作为参数传入函数functionx1 中) ) 
  print(list(filter(functionx1,[10,11,22,30,7])))
    #[11, 7]

  xf = filter(functionx1,[10,11,22,30,7,79])
  print(xf)
    #<filter object at 0x7fcc04fa14e0>

  print(type(xf))
    #<class 'filter'>

  print(list(xf))
    #[11, 7, 79]
                      ## 使用 lambda 匿名函数
  for i in filter(lambda n: n %2, [num*3 for num  in range(9)]):
    print(i,end = '\t')
  #3	9	15	21

  print('\n--------------\n')


def  maptest():

  def  square(x):
    return x ** 2   # 计算平方数
  
  print(map(square, [ 1,2,3,4 ]))
    #<map object at 0x7f09e0ba0128>
  
  print(list(map(square, [ 1,2,3,4 ]))) # 计算列表各个元素的平方
    #[1, 4, 9, 16]               # 计算平方数的结果
  
  print(type(map(square, [ 1,2,3,4 ])))
    #<class 'map'>
  
                     # 使用 lambda 匿名函数 x * y 乘法
        # 提供了两个列表，对相同位置的列表元素 进行 乘法运算
  
  xx = map(lambda x, y: x * y, [1, 2, 3, 4], [10, 20, 30, 40])
  
  print(xx)
    #<map object at 0x7f09e0ba0128>
  print(type(xx))
    #<class 'map'>

  print(list((xx)))
    #[10, 40, 90, 160]   #计算两个列表的每个对应相同索引位置 的元素间相乘的结果
  
  print(list((xx)))
    #[]

def   reducetest():

  def add(x, y):
    return x+y

  print(type(reduce(add, [1,2,3,4])))
    #<class 'int'>

  print(reduce(add, [1,2,3,4]))
    #10
  x = reduce(lambda x, y: x * 10 + y, [1 , 2, 3, 4, 5])

  print(x)
    # 12345
  print(type(x))
    #<class 'int'>

def  functpartial():
  x, y, z = 10, 22, 33
  def add(x, y, z):
    return  x+y+z

  print('add(%d,%d,%d) ---- %d' % (x,y,z, add(x,y,z)))
    #add(10,22,33) ---- 65

#一个带有多个参数的函数,如果其中某些参数基本上固定的,
#那么就可以通过偏函数为这些参数赋默认值

  myadd = partial(add, x = 11, y=200) 
   #偏函数partial(函数名,参数1,参数2)

  print(myadd(z =  3000))
    #3211

  print(myadd(z =  400))
    # 611

def  tkintertest():
  root = tkinter.Tk()
  labl = tkinter.Label(root, text='hello world!', font = 'Helvetica 26 bold italic')
 
#  labl = tkinter.Label(root, text='hello world!', font = 'Aria 36 bold') 
 
  b1 = tkinter.Button(root, bg ='pink', fg = 'green',text= 'Button 1')
  
     ##偏函数partial(函数名,参数1,参数2,参数3)
  mybutton = partial(tkinter.Button, root, bg ='blue', fg = 'white')
  
  b2 = mybutton(text = 'Button 2')
  b3 = mybutton(text = 'QUIT', command = root.quit)
  labl.pack()
  b1.pack()
  b2.pack()
  b3.pack()
  root.mainloop()
  

def   recursionsort():

  def  func1(n):
    if n == 1:
      return n
    return  n * func1(n -1)

  print(func1(5))
  print('\n============================ \n')

# [11]  [22]  33  44  [55]  66  [77]  88  [99]
#  nums = [random.randint(1,100) for i in range(10)]
  nums = [77, 11, 77, 99, 55, 22, 55]
  print('nums ---------------',nums)

  def  randomsort(data):
    count = 0
    itemcount = 0
    if len(data) == 0 or len(data) == 1:
      print('---@len(data) -- %d ---data = %s ---' % (len(data), data))
      return  data
    middle = data.pop()  
    print('middle  is ----------- %d' % middle)
    smaller = []
    larger = []
    for item in  data: 
      if item > middle:
        print('--- item > middle --item is %d ' % item )
        larger.append(item)
      else:
        print('--- item <= middle --item is %d ' % item )
        smaller.append(item)
      itemcount += 1
    count += 1
    print('\t--- count = %d ---\n--- itemcount = %d\n' % (count, itemcount))
    print('\n--- smallerlist is %s---- middle is %d ---larger list is %s --\n' \
      % (smaller, middle, larger))
    return  randomsort(smaller) + [middle] + randomsort(larger)
  
  print('randomsort(nums) --------',randomsort(nums))
  print('end -------nums-------',nums)




if __name__ == '__main__':
  print('\033[30;43;1m sys.argv  is %s\033[0m\n' % sys.argv)  
#  lambdaxy()
#  filterfunlist()
#  maptest()
#  reducetest()
#  functpartial()
#  tkintertest()
  recursionsort()



