# cp /usr/share/pixmaps/faces/fish.jpg .
fobj = open('fish.jpg', 'rb')  # b表示binary二进制方式
print(fobj.read(10))
fobj.close()

