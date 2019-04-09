#!/usr/bin/env  python3
import  sys, random
"MoBan ------------ instruction"

# nlist = [random.randint(1,100) for i in range(10)]
# randomsort(nlist)

def  randomsort(data):
  count = 0
  itemcount = 0
  data = list(data) ##注意是把字典的 键 集合成一个新列表,不包含值

  if len(data) == 0 or len(data) == 1:
    print('---@len(data) -- %d ---data = %s --' % (len(data), data))

    return  data
  middle = data.pop()  
  print('middle  is ----------- %s' % middle)

  smaller = []
  larger = []
  for item in  data: 
    if item > middle:
      print('--- item > middle --item is %s ' % item )

      larger.append(item)
    else:
      print('--- item <= middle --item is %s ' % item )
  
      smaller.append(item)
    itemcount += 1
  count += 1
  print('--- count = %d ---\n--- itemcount = %d\n' % (count, itemcount))


  print('\n---smallerlist is %s----middle is %s ---largerlist is %s--\n' \
    % (smaller, middle, larger))

  return  randomsort(smaller) + [middle] + randomsort(larger)





if __name__ == '__main__':
  print('\033[30;43;1m sys.argv  is %s\033[0m\n' % sys.argv) 

  nlist = [random.randint(1,100) for i in range(10)]

  print('nlist ---------------',nlist)

  print('\nrandomsort(nlist) --- %s\n' % randomsort(nlist))

  print('end -------nlist-------',nlist)

  print('\n~~~~~~~~~~======  nlist =======~~~~~~~~\n')

  astr ='qwertyuiop'
  print(''.join(randomsort(astr))) #把列表通过空字符''拼接在一起
  
  print('\n~~~~~~~~~~======  astr =======~~~~~~~~\n')

  atuple = (10, 331, 55, 99, 77)
  print(tuple(randomsort(atuple))) ##列表转 元组类型
  print('\n~~~~~~~~~~======  atuple =======~~~~~~~~\n')









