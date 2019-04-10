#!/usr/bin/env  python3
import  sys, random
import  tkinter    # tk-devel  tcl-devel 是模版tkinter依赖的软件包
from functools import partial

"MoBan ------------ instruction"

# nlist = [random.randint(1,100) for i in range(10)]
#L = Local     局部作用域
#E = Enclosing 嵌套作用域
#N = nonlocal  只作用于嵌套作用域，而且只是作用在函数里面
#G = global    全局作用域
#B = Built-in  内置作用域



def  countinside(start = 0):
  count = start
  def  incount():
    nonlocal count  # #nonlocal只作用于嵌套作用域，且只作用在函数里面
    count += 1
    return count
  return  incount

def  tkinterinside():

  root = tkinter.Tk()
  labl = tkinter.Label(root, text='hello world!', font = 'Helvetica 26 bold italic')
 
#  labl = tkinter.Label(root, text='hello world!', font = 'Aria 36 bold') 
 
#  def  hello():
#    labl.config(text = 'hello peri')
  
#  def welcome():
#    labl.config(text = 'hello boy')    

#  b1 = tkinter.Button(root, bg ='pink', fg = 'green',text= 'Button 1',  command = hello )

  def  say_hi(words = 'boy!'):
    def  welcome():
      labl.config( text = 'hello %s !' % words)
    return  welcome


  b1 = tkinter.Button(root, bg ='pink', fg = 'green',text= 'Button 1',  command = say_hi('peri') )
  
     ##偏函数partial(函数名,参数1,参数2,参数3)
  mybutton = partial(tkinter.Button, root, bg ='blue', fg = 'white')
  
  b2 = mybutton(text = 'Button 2', command = say_hi() )
  b3 = mybutton(text = 'Button 3', command = say_hi('girls') )

  b4 = mybutton(text = 'QUIT', command = root.quit)
  labl.pack()
  b1.pack()
  b2.pack()
  b3.pack()
  b4.pack()
  root.mainloop()
  
  


if __name__ == '__main__':
  print('\033[30;43;1m sys.argv  is %s\033[0m\n' % sys.argv) 

  a = countinside()
  b = countinside(10)
  print('a  is --- ', a)
  print('a()  is --- ', a())
  print('b() is --- ', b())

  tkinterinside()




