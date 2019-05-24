# tkinter和sqlite3都是python自带的功能，但是可能因为环境不满足无法导入
# yum install -y tk-devel tcl-devel  ->  tkinter需要
# yum install -y sqlite-devel   -> sqlite需要
# 把python重新编译即可
# [root@room8pc16 software]# tar xzf py3soft.tar.gz
# [root@room8pc16 software]# cd pysoft/py3env/
# [root@room8pc16 py3env]# bash setup.sh
import tkinter
from functools import partial

root = tkinter.Tk()
lb1 = tkinter.Label(root, text="hello world!", font = "Aria 16 bold")
b1 = tkinter.Button(root, bg='blue', fg='white', text="Button 1")
mybutton = partial(tkinter.Button, root, bg='blue', fg='white')
b2 = mybutton(text='Button 2')
b3 = mybutton(text='QUIT', command=root.quit)
lb1.pack()
b1.pack()
b2.pack()
b3.pack()
root.mainloop()
