import sys

def copy(src_fname, dst_fname):
    src_fobj = open(src_fname, 'rb')
    dst_fobj = open(dst_fname, 'wb')

    while True:
        data = src_fobj.read(4096)
        if data == b'':
            break
        dst_fobj.write(data)

    src_fobj.close()
    dst_fobj.close()

# copy('/usr/bin/ls', '/tmp/list')
copy(sys.argv[1], sys.argv[2])
