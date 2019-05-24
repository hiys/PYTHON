import sys
import os
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(__file__)   # run.py
# __file__表示文件本身run.py
# abspath取出绝对路径"/var/ftp/py2018/py1801/day11/demo/bbb/run.py"
# os.path.dirname(os.path.abspath(__file__)取出
# /var/ftp/py2018/py1801/day11/demo/bbb
print(BASEDIR)
sys.path.insert(0, BASEDIR)

import aaa.hi

print(aaa.hi.name)

from aaa.hi import name
print(name)
