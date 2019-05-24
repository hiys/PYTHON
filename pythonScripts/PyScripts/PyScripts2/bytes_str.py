str1 = 'abcd'
bstr1 = bytes(str1, encoding='utf8')  # 将utf8字符转成bytes类型
print(bstr1)

str2 = str(bstr1, encoding='utf8')  # 将bytes类型转成str，编码是utf8
print(str2)

