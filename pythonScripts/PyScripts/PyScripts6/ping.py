# 扫描网络中存活主机
import subprocess
import time

def ping(host):
    rc = subprocess.call(
        'ping -c2 %s &> /dev/null' % host, shell=True
    )
    if rc == 0:
        return "%s: up" % host
    else:
        return "%s: down" % host

if __name__ == '__main__':
    hosts = ['172.40.3.%s' % i for i in range(1, 255)]
    start = time.time()
    for ip in hosts:
        print(ping(ip))
    end = time.time()
    print(end - start)
