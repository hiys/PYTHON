# yum install -y sqlite-devel tk-devel tcl-devel readline-devel zlib-devel gcc gcc-c++ openssl-devel libffi-devel
# tar xzf Python-3.6.7.tgz
# cd Python-3.6.7
# ./configure --prefix=/usr/local/
# make && make install


  yum  -y  install  \
 sqlite-devel    tk-devel        tcl-devel       readline-devel   \
 zlib-devel      gcc             gcc-c++         openssl       openssl-devel \
 libffi-devel    libxml2-devel   libxslt-devel   mysql-devel  \
 mariadb-devel   mariadb-server  mariadb 


rpm  -q  \
 sqlite-devel    tk-devel        tcl-devel       readline-devel   \
 zlib-devel      gcc             gcc-c++         openssl       openssl-devel \
 libffi-devel    libxml2-devel   libxslt-devel   mysql-devel  \
 mariadb-devel   mariadb-server  mariadb 

tar  -zxf  Python-3.6.7.tgz 

cd  Python-3.6.7/

./configure   --prefix=/usr/local/

 make && make install



# cp   '/root/桌面/Django-1.11.20.tar.gz' .

# cd
# mkdir    Django    #创建项目目录
 # cd       Django/

ll   /root/Django-1.11.20.tar.gz 

 md5sum   /root/Django-1.11.20.tar.gz

 pip3.6   install   /root/Django-1.11.20.tar.gz 

pip3  freeze   #查看 安装的所有软件包

python3  -m   django  version

pip3  freeze  > pkg1120.txt #导出信息到文件中

cat    pkg1120.txt

--------------- 创建自定义的 干净 虚拟环境 ------------------
------------- python3.6  -m   venv   新目录名 -------------------

 # python3.6  -m   venv   django1120

 ls   django1120/

---------------------- 激活  虚拟环境 ---------------

ll   django116/bin/activate

source    django116/bin/activate    #激活  虚拟环境 

pip  freeze   #查看在虚拟环境中安装的所有软件包

pip  install  $(cat  pkg1120.txt)  #安装模块

pip   install  --upgrade  pip   #升级 pip3版本

 pip  --version

python  --version

django-admin   startproject  mysite   #新建一个django 项目

cd  mysite/   #进入项目

pwd

 python   manage.py   runserver   8800  #开启 django网站 服务


Starting development server at http://127.0.0.1:8800/
Quit the server with CONTROL-C.
^C(django116) [root@V0 mysite]# exit
登出


# cd  Django/


source    django1120/bin/activate    #激活  虚拟环境 

pip  freeze   #查看在虚拟环境中安装的所有软件包

cd   mysite/   #进入网站目录

 python   manage.py   runserver   8800   #开启 django网站 服务


 http://127.0.0.1:8800/ 在火狐浏览器中访问本机



[root@room9pc01 mysite]# pip3.6   install   tornado

Looking in indexes: http://pypi.doubanio.com/simple/
.......................
Installing collected packages: tornado
  Running setup.py install for tornado ... done
Successfully installed tornado-6.0.2

[root@room9pc01 mysite]# pip3  freeze
Django==1.11.20
PyMySQL==0.9.3
pytz==2019.1
SQLAlchemy==1.3.3
tornado==6.0.2
[root@room9pc01 mysite]# pwd
/root/Django/mysite
[root@room9pc01 mysite]# 


Linux服务器下安装python3，pip3
yum -y install
 zlib-devel    bzip2-devel    openssl-devel       ncurses-devel
 sqlite-devel  readline-devel tk-devel gdbm-devel db4-devel
 libpcap-devel xz-devel

然后去官网下载 python3.6.7








