from mktxtfile import get_contents

width = 48

contents = get_contents()
print('+%s+' % ('*' * 48))
for line in contents:
    print('+{:^48}+'.format(line))
print('+%s+' % ('*' * 48))
