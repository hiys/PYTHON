# 全局变量从它定义的位置开始，到程序结尾都是可见可用
x = 10
def foo():
    print(x)
foo()   # 打印出10

def bar():
    x = 'hello world!'  # 局部变量，它遮盖住了全局的x
    print(x)

bar()  # 输出hello world
print(x)  # 输出10

def foo_bar():
    global x   # 引用全局变量x
    x = 100
    print(x)  # 输出100

print(x)  # 输出100

# 名称的搜索顺序依次是局部、全局、内建
print(len('abcd'))  # 4
len = 100
print(len)  # 100
def func1():
    len= [10, 20, 30]
    print(len)

func1()  # [10, 20, 30]

# 函数的参数也是局部变量，传参的时候是把相应的常量传进去，返回值也是常量
def get_info(name, age):
    print('%s is %s years old' % (name, age))
    result = 'OK'
    return result  # 返回字符串OK，而不是返回变量result

name = 'bob'  # 此处的name和函数的参数name没有关系
age = 25
a = get_info(name, age)  # 不会把变量name和age传过去，而是把bob和25传过去
print(a)
