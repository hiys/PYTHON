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
import os, requests, sys
sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

def has_new_version(local_ver_path, live_ver_url):
  pass


def  get_ver(url):
  header = {
    'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
  }
  r = requests.get(url, headers=header)
  print(type(r), r, sep='\n',end='\n\n')
  ver = r.text.strip()  # 获取最新软件的版本号
  return  ver

def   download():
  pass




def check_md5(fname):
  pass



def deploy_web(local_app_path):
  pass








if __name__ == "__main__":
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)

  ver = get_ver('http://192.168.1.11/deploy/live_version')
  print('\nver = %s\n' % ver)






