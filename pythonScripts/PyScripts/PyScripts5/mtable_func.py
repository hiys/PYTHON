def gen_mtable():
    for i in range(1, 10):    # [0, 1, 2]
        for j in range(1, i+1): # i->0:[0], i->1: [0, 1], i->2: [0, 1, 2]
            print('%sX%s=%s' % (j, i, i*j), end=' ')
        print()

gen_mtable()
