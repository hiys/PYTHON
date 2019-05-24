# 100块钱，买100只鸡。公鸡５块钱，母鸡３块钱，３只小鸡共１块钱
# x+y+z=100  5x+3y+z/3=100
# z=100-x-y  5x+3y+(100-x-y)/3=100
import time

start = time.time()
for x in range(21):
    for y in range(34):
        z = 100 - x - y
        if x * 5 + y * 3 + z / 3 == 100:
            print(x, y, z)
end = time.time()
print(end - start)
