#!/usr/bin/env  python3
import  sys, random
"MoBan ------------ instruction"

# nums = [99, 55, 22, 55]
# randomsort(nums)

def  randomsort(data):
  count = 0
  itemcount = 0
  if len(data) == 0 or len(data) == 1:
    print('---@len(data) -- %d ---data = %s --' % (len(data), data))

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
  print('--- count = %d ---\n--- itemcount = %d\n' % (count, itemcount))


  print('\n---smallerlist is %s----middle is %d ---largerlist is %s--\n' \
    % (smaller, middle, larger))

  return  randomsort(smaller) + [middle] + randomsort(larger)




#  nlist2 = [77, 99, 55, 22, 55]
#  randomsort_2(nlist2)

def  randomsort_2(data):
  count = 0
  itemcount = 0
  if len(data) == 0 or len(data) == 1:
    print('---@len(data) -- %d ---data = %s --' % (len(data), data))


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
  print('--- count = %d ---\n--- itemcount = %d\n' % (count, itemcount))


  print('\n---smallerlist is %s----middle is %d ---largerlist is %s--\n' \
    % (smaller, middle, larger))

  return  randomsort_2(smaller) + [middle] + randomsort_2(larger)



#  nlist3 = [11, 77, 99, 55, 22, 55]
#  randomsort_3(nlist3)

def  randomsort_3(data):
  count = 0
  itemcount = 0
  if len(data) == 0 or len(data) == 1:
    print('---@len(data) -- %d ---data = %s --' % (len(data), data))


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
  print('--- count = %d ---\n--- itemcount = %d\n' % (count, itemcount))


  print('\n---smallerlist is %s----middle is %d ---largerlist is %s--\n' \
    % (smaller, middle, larger))

  return  randomsort_3(smaller) + [middle] + randomsort_3(larger)




if __name__ == '__main__':
  print('\033[30;43;1m sys.argv  is %s\033[0m\n' % sys.argv) 

  nums = [99, 55, 22, 55]
  print('nums ---------------',nums)

  print('\nrandomsort(nums) --- %s\n' % randomsort(nums))

  print('end -------nums-------',nums)

  print('\n ================= nums ~~~~~~~~~~~~~~~\n')



  nlist2 = [77, 99, 55, 22, 55]
  print('nlist2 ---------------',nlist2)

  print('\nrandomsort_2(nlist2) --- %s\n' % randomsort_2(nlist2))

  print('end -------nlist2----- %s' % nlist2)

  print('\n~~~~~~~~~~~~~~~~~~ nlist2 ==============\n')



  nlist3 = [11, 77, 99, 55, 22, 55]
  print('nlist3 ---------------',nlist3)

  print('\nrandomsort_3(nlist3) --- %s\n' % randomsort_3(nlist3))

  print('end -------nlist3-------',nlist3)

  print('\n~~~~~~~~~~======  nlist3 =======~~~~~~~~\n')




