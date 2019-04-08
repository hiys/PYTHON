#!/usr/bin/env  python3
import  sys, os, pickle, time, random
"MoBan ------------ instruction"
print('\033[31;47;1m__name__  is %s\033[0m' %  __name__)

#def  additive(x, y):  #[数]加法
#  return  x + y

#def  subtraction(x, y):  #减法
#  return  x - y

def  exam():
#  cmds = { '+': additive, '-': subtraction }  # 将函数存入字典
  cmds = { '+': lambda  x, y: x + y , '-': lambda  x, y: x - y }  #将#匿名函数存入字典
  nums = [ random.randint(1,100) for i in range(2) ] # 生成两个数
  nums.sort(reverse=True)  # 降序排列(从大 到小)
  op = random.choice('+-')
  result = cmds[op](*nums)  # 调用存入字典的函数，把nums列表拆开，作为参数传入
  prompt = "%s %s %s = " % (nums[0], op, nums[1])
  trynums = 0 #尝试次数
  while trynums < 3:
    try:
      answer = int(input(prompt))
    except:  #不论任何异常,均跳过异常,不推荐使用
      continue
    print('\nexam()方法的 异常捕获程序结束之后\n \
    当前面出现 "except 语句" 所 没有捕获到的异常后,本语句也不会执行---')
    if answer == result:
      print('你真棒，答对了！')
      break  # 答对了就不要再回答了，结束循环
    else:
      print('答错了')
      trynums += 1
      if trynums == 2:
        print('-------- 最后一次机会了------------')
  else:  
    print("正确的解答是 %s%s" % (prompt, result))   # 这里当循环不被break时才执行


def main():
  while True:
    exam()
    try:
      go_on = input('Continue(y/n)? ').strip()[0]
    except IndexError:  #序列中没有没有此索引,空输入
      continue
    except (KeyboardInterrupt, EOFError):
      go_on = 'n'
    print('\nmain() 方法的 异常捕获程序结束之后\n \
    当前面出现 "except 语句" 所 没有捕获到的异常后,本语句也不会执行---')
    if go_on in 'nN':
      print('\nBye-bye.')
      break



if __name__ == '__main__':
  print('\033[30;43;1m sys.argv  is %s\033[0m\n' % sys.argv)  
  main()


