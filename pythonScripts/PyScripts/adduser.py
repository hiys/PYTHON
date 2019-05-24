import sys
import subprocess
from randpass2 import gen_pass  # cp day05/randpass2.py .

def add_user(username, password, fname):
    info = """user information:
username: %s
password: %s
"""
    subprocess.call('useradd %s' % username, shell=True)
    subprocess.call(
        'echo %s | passwd --stdin %s' % (password, username),
        shell=True
    )

    with open(fname, 'a') as fobj:
        fobj.write(info % (username, password))


if __name__ == '__main__':
    username = sys.argv[1]
    password = gen_pass()
    fname = '/tmp/users.txt'
    add_user(username, password, fname)



