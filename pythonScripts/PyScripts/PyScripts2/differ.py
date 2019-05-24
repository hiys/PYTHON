# mkdir /tmp/demo
# cp /etc/passwd /tmp/demo
# cp /etc/passwd /tmp/demo/mima
# gedit /tmp/demo/mima  删除和添加一些行

with open('/tmp/demo/mima') as today:
    set1 = set(today)

with open('/tmp/demo/passwd') as yestoday:
        set2 = set(yestoday)

print(set1 - set2)

with open('/tmp/result.txt', 'w') as fobj:
    fobj.writelines(set1 - set2)  # cat /tmp/result.txt
