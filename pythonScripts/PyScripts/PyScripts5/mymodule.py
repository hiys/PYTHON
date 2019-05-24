import time, datetime  # 不推荐，每个模块占一行，多行导入
from random import randint, choice  # 导入模块中的某些功能
import pickle as p  # 导入模块，同时为其设置别名

a = randint(1, 10)
op = choice('+-*/')
# random.randint(1, 10)  没有导入random，此种方式不可行
p.dumps(100)
