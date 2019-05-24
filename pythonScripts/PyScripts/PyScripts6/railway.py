import time
import sys

print('#' * 20, end='')
n = 0

while True:
    print('\r%s@%s' % ('#' * n, '#' * (19 - n)), end='')
    sys.stdout.flush()
    n += 1
    time.sleep(0.3)
    if n == 19:
        n = 0
