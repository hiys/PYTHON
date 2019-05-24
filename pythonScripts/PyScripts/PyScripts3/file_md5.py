import hashlib
# with open('/etc/passwd', 'rb') as fobj:
#     data = fobj.read()
#
# m = hashlib.md5(data)
# print(m.hexdigest())
def check_md5(fname):
    m = hashlib.md5()
    with open(fname, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexdigest()

if __name__ == '__main__':
    print(check_md5('/etc/passwd'))
