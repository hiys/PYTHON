#!/usr/bin/env  python3
import  sys, os, pickle, time

print('\033[31;47;1m__name__  is %s\033[0m' %  __name__)

# 日期　　开销　　收入　　余额　　备注
# sys.argv[1] = 'record.txt'   # 记帐文件
# sys.argv[2] = 'wallet.data'  # 记录余额

try:
  record = '/root/桌面/Test/' + sys.argv[1]
  wallet = '/root/桌面/Test/' + sys.argv[2]
except  IndexError as  FirstEr:
  print('\n序列中没有没有此索引,可能位置参数缺失FirstEr--\t',FirstEr)


def  accountest():
  pass  # pass语句在函数中的作用
#空语句 do nothing
#保证格式完整
#保证语义完整
#定义一个函数account，
#但函数体部分暂时还没有完成，又不能空着不写内容，
#因此可以用pass来替代占个位置。

## 日期date　　开销amount　　收入income　　余额balance　　备注comment

date = time.strftime('%Y年*%m月*%d日  %H时:%M分:%S秒',time.localtime())
amount = 0      #开销费用
revenue = 0     #后面新增加的收入
income = 10000   #原始收入
balance = 10000  #总余额
comment = ''     #备注

def  spend_money(record,wallet):
  date = time.strftime('%Y年*%m月*%d日  %H时:%M分:%S秒',time.localtime())
  amount = int(input('消费额: '))
  comment = input('备注: ')
  revenue = 0
  with  open(wallet,'rb') as frobj:
    balance = pickle.load(frobj) - amount

  with  open(wallet,'wb') as fwobj:
    pickle.dump(balance, fwobj)

  with open(record, 'a') as  fobj:
#('日 期', '开 销', '收 入', '余 额', '备 注')
    fobj.write('%-28s#%-8s#%8s#%-8s#%20s\n' % \
    (date, amount, revenue, balance, comment))

  
def  save_money(record,wallet):
  date = time.strftime('%Y年*%m月*%d日  %H时:%M分:%S秒',time.localtime())
  revenue = int(input('新增加的收入额: '))
  comment = input('备注: ')
  amount = 0

  with  open(wallet,'rb') as frobj:
    balance = pickle.load(frobj) + revenue

  with  open(wallet,'wb') as fwobj:
    pickle.dump(balance, fwobj)

  with open(record, 'a') as  fobj:
#('日 期', '开 销', '收 入', '余 额', '备 注')
    fobj.write('%-28s#%-8s#%8s#%-8s#%20s\n' % \
    (date, amount, revenue, balance, comment))




def   query(record, wallet):
  with  open(record)  as frobj:
    for  line  in  frobj:
      print(line,end='\t')

  with open(wallet,'rb') as frbobj:
     balance = pickle.load(frbobj)
  print('当前余额: %s \n' % balance)



def  show_menu(sysarg1,sysarg2):
  prompt = """(0) 记录开销
(1) 记录收入
(2) 查询收支记录
(3) 退出
请选择(0/1/2/3): """

  cmds = { 0 :spend_money, 1 :save_money, 2 : query }
  if not os.path.exists('/root/桌面/Test'):
    os.makedirs('/root/桌面/Test')
  if os.path.exists(record):
    os.remove(record)
  if os.path.exists(wallet):
    os.remove(wallet)

  with open(wallet, 'wb') as fwobj:
    pickle.dump(income, fwobj)  #原始收入income = 10000

  with  open(record,'w') as fwobj:
    fwobj.write('%-28s#%-8s#%8s#%-8s#%20s\n' % \
      ('日 期', '开 销', '收 入', '余 额', '备 注')
    )

  with open(record, 'a') as  fobj:
#('日 期', '开 销', '收 入', '余 额', '备 注')
    fobj.write('%-28s#%-8s#%8s#%-8s#%20s\n' % \
      (date, amount, income, balance, comment)
    )


  while  True:
    try:
      choice = int(input(prompt).strip()[0])
    except IndexError as thirdEr:
      print('\n序列中没有没有此索引,空输入\t', thirdEr)
    except (KeyboardInterrupt, EOFError):
      print('\n用户ctrl+ d 中断退出^D,用户ctrl+ c 中断执行^C\n')
      break
    else:
      if not 0 <= choice <4 :
        print('无效输入，请重试')
        continue
      if choice == 3:
        break
      cmds.get(choice,'如果不存在对应的键名(比如0123之外的数字),\
会返回此信息')(record,wallet)


if __name__ == '__main__':
  print('\033[30;43;1m sys.argv  is %s\033[0m\n' % sys.argv)
  try:
    print('\033[32;46;1m sys.argv[1] is %s\033[0m' % sys.argv[1])
    accountest()
    show_menu(sys.argv[1],sys.argv[2])
  except  IndexError as  secondEr:
    print('\n序列中没有没有此索引,位置参数缺失---secondEr:\t',secondEr)


