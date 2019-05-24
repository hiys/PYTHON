import pickle as p
shop_file = '/tmp/shop.data'
shop_list = ['eggs', 'apple', 'banana']
f = open(shop_file, 'wb')
p.dump(shop_list, f)  # 将列表写入到文件
f.close()
# ----------------------
f = open('/tmp/shop.data', 'rb')
shop_list = p.load(f)  # 把列表从文件中读出来
f.close()
print(shop_list)  #
