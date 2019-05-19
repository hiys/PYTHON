#/usr/bin/env    python3
#coding:UTF-8
#! -*- coding:utf8 -*-
"""
candidate      英 [ˈkændɪdət]   美 [ˈkændɪdət]  
n.(竞选或求职的)候选人，申请人;投考者;应试者;参加考试的人;被认定适合者;被认定有某种结局者

deploy        英 [dɪˈplɔɪ]   美 [dɪˈplɔɪ]  
    v.部署，调度(军队或武器);有效地利用;调动

deployment     英 [dɪˈplɔɪmənt]
    n.(部队、资源或装备的)部署，调集

delivery    英 [dɪˈlɪvəri]
   n.传送;递送;交付;分娩;演讲方式;表演风格

http://192.168.1.11:8080/job/Myproject_build/configure
Jenkins    Myproject_build
构建
 执行shell 命令
deploy_dir=/var/www/html/deploy/packages/
cp  -r   Myproject_${mptag}   $deploy_dir
rm  -rf   $deploy_dir/Myproject_${mptag}/.git
cd     $deploy_dir
tar   czf    Myproject_${mptag}.tar.gz   Myproject_${mptag}
rm   -rf    Myproject_${mptag}
md5sum    Myproject_${mptag}.tar.gz |awk '{print $1}'> Myproject_${mptag}.tar.gz.md5

创建两个版本文件
– live_version:表示当前使用版本
– last_version:表示上一个版本

http://192.168.1.11:8080/job/mp_live_version/configure
构建
    执行shell 命令

x1="/var/www/html/deploy/"
[ -f  ${x1}live_version ] && cat  ${x1}live_version  > ${x1}last_version
echo  ${mypver} > /var/www/html/deploy/live_version

http://192.168.1.11/deploy/
http://192.168.1.11/deploy/last_version
1.0
http://192.168.1.11/deploy/live_version
2.0

http://192.168.1.11/deploy/packages/
http://192.168.1.11/deploy/packages/Myproject_1.0.tar.gz
http://192.168.1.11/deploy/packages/Myproject_1.0.tar.gz.md5

http://192.168.1.11/deploy/packages/Myproject_2.1.tar.gz
http://192.168.1.11/deploy/packages/Myproject_2.1.tar.gz.md5

[root@V1 ~]# ls  /var/www/html/deploy/
last_version  live_version  packages
[root@V1 ~]# ls  /var/www/html/deploy/packages/
Myproject_1.0.tar.gz      Myproject_2.1.tar.gz
Myproject_1.0.tar.gz.md5  Myproject_2.1.tar.gz.md5

[root@V1 ~]# cat   /var/www/html/deploy/packages/Myproject_1.0.tar.gz.md5 
5bae1cf3cfc66e6d96d8c378473503ac
[root@V1 ~]# cat   /var/www/html/deploy/packages/Myproject_2.1.tar.gz.md5 
2cd0e564d55de2286a4ce6a34d7e29d9
"""
import  os, requests, sys
import  urllib.request, hashlib, tarfile

sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

header = {
  'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
}

def has_new_version(local_ver_path, live_ver_url):
  pass


def  get_webdata(url):
  r = requests.get(url, headers=header)
  print(type(r), r, sep='\n',end='\n\n')
#<class 'requests.models.Response'>
#<Response [200]>
  ver = r.text.strip()  # 获取最新软件的版本号或md5值字符串
  return  ver

def   download(url, fname):
  request = urllib.request.Request(url,headers=header)
  print(request,type(request))  
#<urllib.request.Request object at 0x7f9f9df1d400> <class 'urllib.request.Request'>
  html = urllib.request.urlopen(request)
  print(html, type(html))
#<http.client.HTTPResponse object at 0x7f9f921ec438> <class 'http.client.HTTPResponse'>
  with  open(fname, 'wb') as fobj:
    while True:
      data = html.read(1024)
      if  not  data:
        print("data  is  None ----", data)
        #data  is  None ---- b''
        break
      fobj.write(data)
  print('\n---------- download(url, fname) ---------------\n')



#  print('\n-------------------------\n')
def check_md5(fname):
  m = hashlib.md5()
  with open(fname, 'rb') as fobj:
    while True:
      data = fobj.read(4096)
      if not data:
        break
      m.update(data)
  return m.hexdigest()  #返回md5值字符串


#deploy_dir = '/download/'
#app_path = "/download/Myproject_%s.tar.gz" % ver
#根据linux内核的实现来看，无法查看一个目录是否存在别的软链接链接到它。除非修改内核。

def deploy_web(app_path, deploy_dir):  #部署下载的压缩包
  os.chdir(deploy_dir)  #切换到部署应用的目录deploy_dir
  tar = tarfile.open(app_path, 'r:gz')
  tar.extractall()  #解压下载的压缩包
  tar.close()

  app_path = app_path.replace('.tar.gz', '')    #"Myproject_%s" % ver
  dest_path = '/var/www/html/mysite' #注意这是链接目录，不能用linux命令mkdir创建
#[root@V1 MyProject]# ll  /var/www/html/mysite 
#lrwxrwxrwx 1 root root 23 5月  19 13:56 /var/www/html/mysite -> /download/Myproject_2.1
  if os.path.exists(dest_path):
    os.unlink(dest_path)   # 如果目标链接已存在，先删除再创建
  os.symlink(app_path, dest_path)








if __name__ == "__main__":
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)

#[root@V1 MyProject]# ls  /var/www/html/deploy/packages/
#Myproject_1.0.tar.gz      Myproject_2.1.tar.gz
#Myproject_1.0.tar.gz.md5  Myproject_2.1.tar.gz.md5
#>>> ver = '2.0'
#>>> if  ver == '2.0':
#...   ver =  2.1;
#...   print(ver)
#... 
#2.1
#>>> 
#[root@V1 MyProject]# cat  /var/www/html/deploy/last_version 
#1.0
#[root@V1 MyProject]# cat  /var/www/html/deploy/live_version 
#2.0
#[root@V1 MyProject]# ls  /var/www/html/deploy/
#last_version  live_version  packages
#[root@V1 MyProject]# mkdir  /download
#[root@V1 MyProject]# ls   /download/


  ver = get_webdata('http://192.168.1.11/deploy/live_version')
  print('\nver = %s\n' % ver)
  #ver = 2.0
  if  ver == '2.0':
    ver = '2.1'
  app_name = "Myproject_%s.tar.gz" % ver
  app_url = 'http://192.168.1.11/deploy/packages/' + app_name
  print(app_url)
  #http://192.168.1.11/deploy/packages/Myproject_2.1.tar.gz

  app_path = os.path.join('/download/', app_name)
  download(app_url, app_path)  #下载软件压缩包

  local_md5 = check_md5(app_path)
  print('\n----- local_md5 = %s\n' % local_md5)
#----- local_md5 = 2cd0e564d55de2286a4ce6a34d7e29d9

  remote_md5 = get_webdata(app_url + '.md5')
  print('\nremote_md5 = %s\n' %  remote_md5)
#remote_md5 = 2cd0e564d55de2286a4ce6a34d7e29d9

  deploy_dir = "/download/"  #切换到部署应用的目录deploy_dir

  if  local_md5 == remote_md5 :
    deploy_web(app_path, deploy_dir)  #部署下载的压缩包
    print('\n --------------------\n')






