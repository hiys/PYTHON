import time
import sys

for i in range(1, 6):
    print('\r%s' % i, end='')  # \r回车不换行
    sys.stdout.flush()
    time.sleep(1)
