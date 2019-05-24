import keyword

# 打印所有的关键字
print(keyword.kwlist)
# 判断一个单词，如pass，是不是关键字
print(keyword.iskeyword('pass'))
print('pass' in keyword.kwlist)
