# 100以内的偶数之和
result = 0
counter = 0

while counter < 100:
    counter += 1
    # if counter % 2:     # 非０为真，０为假
    if counter % 2 == 1:
        continue  # 跳过本次循环，循环体内后续代码被跳过，回到判断条件
    result += counter

print(result)

