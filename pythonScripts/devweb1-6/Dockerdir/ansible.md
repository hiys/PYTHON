# docker 安装
ftp://172.40.50.127/py1712/day29-30ansible-docker/

rpm -ivh *.rpm


# aufs

 L1
 L2  a.txt
 L3  rm a.txt


# docker swarm

k8s: kubernetes



import  export


docker run centos
python3


docker save imagename:tag > xxxx.tar.gz




## 启动docker
systemctl start docker

##  导入镜像
docker load < centos-ansible-master.tar.gz

## 启动容器

docker run -itd -h centos-node --name centos-node centos-node:6 


docker ps
docker exec -it fc15ced8519c bash

## 两个容器连接
docker run -itd -h centos-master --name centos-master --link centos-node:centos-node  centos-ansible-master


shadowsocks


tplink  720N  openwrt+uboot   chinadns
luci

netgear r6300v2  梅林
	haproxy


docker ps -a
docker start 

.so
.dll

.rpm
.deb

yum install
apt-get install
#centos 启动ssh
 /etc/init.d/sshd start
#ubuntu 启动ssh
/etc/init.d/ssh start
# 公钥 配置
## master端运行

># ssh-keygen 
># ssh-copy-id root@172.17.0.4
## 客户端机器
cd /root
mkdir .ssh
cd .ssh
vim authorized_keys （粘贴master机器id_rsa.pub内容）


chmod 000

chattr +i  /etc/hosts


nobody  python manage.py runserver 
subprocess("poweroff")








--
-hosts:*node
  vars:
    









ansible-playbook httpd.yml


IPMI
cobbler



lamp: linux+apache+mysql+php
lnmp: linux+nginx+mysql+php

salststack

master:
Minion:




# demo 部署

## 拷贝 cmdb  目录 到 /root下
## 删除现有master容器

	docker stop xxxxxxx
	docker rm xxxxxxx
## 启动新master容器

	docker run -itd -h centos-master --name centos-master -p 8000:8000 -v /root/cmdb:/srv centos-ansible-master

## 进入master容器

ssh-keygen
### 拷贝公钥到node节点
### 修改/etc/ansible/hosts
[node]
172.17.0.2
172.17.0.4

cd /srv/cmdbui
python manage.py runserver 0:8000


a = 5 
$a = 5

lambda 



















