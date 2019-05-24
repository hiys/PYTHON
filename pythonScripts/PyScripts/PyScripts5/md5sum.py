# md5是文件的指纹，相同的源总是能生成固定长度的相同的值。不能通过结果反推出源
# 可用于加密的密码以及文件完整性校验

import hashlib

hello = bytes('hello world', encoding='utf8')
m = hashlib.md5(hello)
print(m.hexdigest())
