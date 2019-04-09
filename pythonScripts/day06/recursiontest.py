#!/usr/bin/env  python3
import  sys, random
"MoBan ------------ instruction"


# nums = [55]
#randomsort(nums)

def  randomsort(data):
  count = 0
  itemcount = 0
  if len(data) == 0 or len(data) == 1:
    print('---@len(data) -- %d ---data = %s --' % (len(data), data))
    #---@len(data) -- 1 ---data = [55] -- #第一轮循环递归

    return  data    #返回结果直接退出当前的函数运行状态,后面的语句都不执行
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
  print('--- count = %d ---\n--- itemcount = %d\n' % (count, itemcount))


  print('\n---smallerlist is %s----middle is %d ---largerlist is %s--\n' \
    % (smaller, middle, larger))

  return  randomsort(smaller) + [middle] + randomsort(larger)




#  nlist2 = [22, 55]
#  randomsort_2(nlist2)

def  randomsort_2(data):
  count = 0
  itemcount = 0
  if len(data) == 0 or len(data) == 1:
    print('---@len(data) -- %d ---data = %s --' % (len(data), data))
    #---@len(data) -- 1 ---data = [22] -- 
        ##第2 轮循环递归 ( 并发同时运行子递归函数randomsort_2(smaller) )
    #---@len(data) -- 0 ---data = [] -- 
        ##第2 轮循环递归 ( 并发同时运行子递归函数randomsort_2(larger) )

    return  data  #返回结果直接退出当前的函数运行状态,后面的语句都不执行
  middle = data.pop()  
  print('middle  is ----------- %d' % middle)
  #middle  is ----------- 55   #第一轮循环递归

  smaller = []
  larger = []
  for item in  data: 
    if item > middle:
      print('--- item > middle --item is %d ' % item )

      larger.append(item)
    else:
      print('--- item <= middle --item is %d ' % item )
      #--- item <= middle --item is 22   #第一轮循环递归
  
      smaller.append(item)
    itemcount += 1
  count += 1
  print('--- count = %d ---\n--- itemcount = %d\n' % (count, itemcount))
  #--- count = 1 ---       #第一轮循环递归
  #--- itemcount = 1

  print('\n---smallerlist is %s----middle is %d ---largerlist is %s--\n' \
    % (smaller, middle, larger))
  #---smallerlist is [22]----middle is 55 ---largerlist is []--  #第一轮循环递归

  return  randomsort_2(smaller) + [middle] + randomsort_2(larger)
  #把所有的子递归函数执行的 if len(data) == 0 or len(data) == 1: 语句中的
  # 返回数据信息的结果一层层分别拼接起来,组成新的数据列表,作为最后的结果输出



#  nlist3 = [55, 22, 55]
#  randomsort_3(nlist3)

def  randomsort_3(data):
  count = 0
  itemcount = 0
  if len(data) == 0 or len(data) == 1:
    print('---@len(data) -- %d ---data = %s --' % (len(data), data))
    #---@len(data) -- 0 ---data = [] --
       ##第2 轮循环递归 ( 并发同时运行子递归函数randomsort_3(larger) )
   #---@len(data) -- 1 ---data = [55] -- ##第3 轮循环递归 ( 并发同时运行子递归函数randomsort_3(larger) )
   #---@len(data) -- 0 ---data = [] -- ##第3 轮循环递归( 并发同时运行子递归函数randomsort_3(smaller) )

    return  data
  middle = data.pop()  
  print('middle  is ----------- %d' % middle)
  #middle  is ----------- 55  #第一轮循环递归
 #middle  is ----------- 22 ##第2 轮循环递归( 并发同时运行子递归函数randomsort_3(smaller) )

  smaller = []
  larger = []
  for item in  data: 
    if item > middle:
      print('--- item > middle --item is %d ' % item )
      #--- item > middle --item is 55
        ##第2 轮循环递归( 并发同时运行子递归函数randomsort_3(smaller) )


      larger.append(item)
    else:
      print('--- item <= middle --item is %d ' % item )
      #--- item <= middle --item is 55  #第一轮循环递归
      #--- item <= middle --item is 22  #第一轮循环递归
  
      smaller.append(item)
    itemcount += 1
  count += 1
  print('--- count = %d ---\n--- itemcount = %d\n' % (count, itemcount))
  #--- count = 1 ---    #第一轮循环递归
  #--- itemcount = 2    #第一轮循环递归
 #--- count = 1 ---   ##第2 轮循环递归(并发同时运行子递归函数randomsort_3(smaller))
 #--- itemcount = 1

  print('\n---smallerlist is %s----middle is %d ---largerlist is %s--\n' \
    % (smaller, middle, larger))
  #---smallerlist is [55, 22]----middle is 55 ---largerlist is []--  #第一轮循环递归
  #---smallerlist is []----middle is 22 ---largerlist is [55]--
       ##第2 轮循环递归(并发同时运行子递归函数randomsort_3(smaller))

  return  randomsort_3(smaller) + [middle] + randomsort_3(larger)
  #把所有的子递归函数执行的 if len(data) == 0 or len(data) == 1: 语句中的
  # 返回数据信息的结果一层层分别拼接起来,组成新的数据列表,作为最后的结果输出



if __name__ == '__main__':
  print('\033[30;43;1m sys.argv  is %s\033[0m\n' % sys.argv) 

  nums = [55]
  print('nums ---------------',nums)
  #nums --------------- [55]

  print('\nrandomsort(nums) --- %s\n' % randomsort(nums))
  #randomsort(nums) --- [55]

  print('end -------nums-------',nums)
  #end -------nums------- [55]

  print('\n ==================== nums ~~~~~~~~~~~~~~~\n')
  # ==================== nums ~~~~~~~~~~~~~~~



  nlist2 = [22, 55]
  print('nlist2 ---------------',nlist2)
  #nlist2 --------------- [22, 55]

  print('\nrandomsort_2(nlist2) --- %s\n' % randomsort_2(nlist2))
  #randomsort_2(nlist2) --- [22, 55]

  print('end -------nlist2----- %s' % nlist2)
  #end -------nlist2----- [22]

  print('\n ==================== nlist2 ~~~~~~~~~~~~~~~\n')
  # ==================== nlist2 ~~~~~~~~~~~~~~~



  nlist3 = [55, 22, 55]
  print('nlist3 ---------------',nlist3)
  #nlist3 --------------- [55, 22, 55]

  print('\nrandomsort_3(nlist3) --- %s\n' % randomsort_3(nlist3))
  #randomsort_3(nlist3) --- [22, 55, 55]

  print('end -------nlist3-------',nlist3)
  #end -------nlist3------- [55, 22]

  print('\n ~~~~~~~~~~~~~~~~~~ nlist3 ================\n')
  # ~~~~~~~~~~~~~~~~~~ nlist3 ================




