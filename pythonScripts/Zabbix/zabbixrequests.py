#/usr/bin/env    python3
#coding:UTF-8
#! -*- coding:utf8 -*-
"""#coding=UTF-8
https://www.zabbix.com/documentation/3.4/zh/manual
Zabbix 手册
欢迎使用Zabbix 3.4软件使用手册，
本手册可以帮助用户利用Zabbix实现对从简单到复杂的监控任务的高效管理。

precondition    英 [ˌpriːkənˈdɪʃn]
    n.先决条件;前提
frontend   前端;前台;前端模块;前段;编译器前端

https://www.zabbix.com/documentation/3.4/zh/manual/api/reference/user/login
Source
CUser::login() in frontends/php/include/classes/api/services/CUser.php.
\w 匹配字母或数字或下划线_
\s 匹配任意的空白符 
\d 匹配数字    等价于[0-9]

[root@V3 zabbix]# grep  -Pnv  '^(\s*)(\*|\/|$)'   /usr/share/zabbix/include/classes/api/services/CUser.php 

"""
import  requests, json, sys

sys.stdout.write('\033[32;46;1m__name__ is %s\n\033[0m' % __name__)

url = 'http://192.168.0.13/zabbix/api_jsonrpc.php'
header = {'Content-Type' : 'application/json-rpc'}

data = {
  "jsonrpc": "2.0",    #jsonrpc协议版本号
  "method": "apiinfo.version",       #zabbix手册上查询版本号
  'id': 1,              #随便写的数字,测试操作使用
  'auth': None,         #不需要身份验证
  "params": {}          #没有额外的参数
}

datajs = json.dumps(data)  #转成 json 格式
print(type(datajs), datajs, sep='\n', end='---------datajs\n')
#<class 'str'>
#{"jsonrpc": "2.0", "method": "apiinfo.version", "id": 1, "auth": null, "params": {}}---------datajs



response = requests.post(url, headers=header, data=datajs)
print(response.json(),end = '  -----1\n')    #zabbix返回 json格式的数据
#{'jsonrpc': '2.0', 'result': '3.4.15', 'id': 1}  -----1
print('*-' * 10, end='\n\n')
#*-*-*-*-*-*-*-*-*-*-
data = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": "admin",
        "password": "zabbix"
    },
    "id": 1
}
datajs = json.dumps(data)  #转成 json 格式
print(type(datajs), datajs, sep='\n', end='---------datajs\n')
#<class 'str'>
#{"jsonrpc": "2.0", "method": "user.login", "params": {"user": "admin", "password": "zabbix"}, "id": 1}---------datajs

response = requests.post(url, headers=header, data=datajs)
print(response.json(),end = '  -----2admin\n')    #zabbix返回 json格式的数据
#{'jsonrpc': '2.0', 'result': '3e3a43c642d776e22f9ebed8c0d19c5d', 'id': 1}  -----2admin


print('*-*' * 10, end='\n\n')
#*-**-**-**-**-**-**-**-**-**-*
data = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": "Admin",
        "password": "zabbix"
    },
    "id": 2
}
datajs = json.dumps(data)  #转成 json 格式
print(type(datajs), datajs, sep='\n', end='---------datajs\n')
#<class 'str'>
#{"jsonrpc": "2.0", "method": "user.login", "params": {"user": "Admin", "password": "zabbix"}, "id": 2}---------datajs

response = requests.post(url, headers=header, data=datajs)
print(response.json(),end = '  -----3Admin\n')    #zabbix返回 json格式的数据
#{'jsonrpc': '2.0', 'result': 'b8df3102cb88beefa0b13ccb5e20eec7', 'id': 2}  -----3Admin

print('$-' * 10, end='\n\n')
#$-$-$-$-$-$-$-$-$-$-

data = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": "root",
        "password": "zabbix"
    },
    "id": 1
}
datajs = json.dumps(data)  #转成 json 格式
print(type(datajs), datajs, sep='\n', end='---------datajs\n')
#<class 'str'>
#{"jsonrpc": "2.0", "method": "user.login", "params": {"user": "root", "password": "zabbix"}, "id": 1}---------datajs

response = requests.post(url, headers=header, data=datajs)
print(response.json(),end = '  -----4root\n')    #zabbix返回 json格式的数据
#{'jsonrpc': '2.0', 'error': {'code': -32602, 'message': 'Invalid params.', 'data': 'Login name or password is incorrect.'}, 'id': 1}  -----4root



if __name__ == "__main__":
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)



