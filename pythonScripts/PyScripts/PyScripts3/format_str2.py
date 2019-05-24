'{} is {} years old'.format('bob', 23)  # 两个参数替换前面的{}
'{1} is {0} years old'.format(23, 'bob')  # 23对应{0}, bob -> {1}
'{0} is {0} years old'.format(['bob', 23]) # {0} -> ['bob', 23]
'{0[0]} is {0[1]} years old'.format(['bob', 23])
'{0[name]} is {0[age]} years old'.format({'name': 'bob', 'age': 23})
"{0:12}{1:8}".format('name', 'age')  # name占12宽度，左对齐
"{0:>12}{1:>8}".format('name', 'age')  # 右对齐
"{0:^12}{1:^8}".format('name', 'age')  # 居中
"{0:#>12}{1:#>8}".format('name', 'age')  # 用#代替空格进行填充

