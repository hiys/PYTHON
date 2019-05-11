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

https://www.zabbix.com/documentation/3.4/zh/manual/api/reference/host/get
host.get
Description 说明
integer/array host.get(object parameters)
此方法允许根据指定的参数获取主机。

Parameters参数
(object) 定义期望输出的参数
该方法支持以下参数。
参数            类型            说明
filter	object	仅返回完全匹配指定筛选后的结果。
接受一个数组，其键值为属性名，其值要么是一个单一的值，要么是一个匹配的数组值。 
Allows filtering by interface properties.允许通过接口属性筛选。

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


print('$-$' * 10, end='\n\n')
print('----检索所有的主机 -------------------\n')

url = 'http://192.168.0.13/zabbix/api_jsonrpc.php'
header = {'Content-Type' : 'application/json-rpc'}

#{'jsonrpc': '2.0', 'result': '198868f7543830d22a4f9845a75fd495', 'id': 1}  -----2admin
#检索所有关于主机名为“Zabbix server”和“Linux server”的数据。

data = {
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": "extend",
        "filter": {     #过滤指定要显示的主机信息
            "host": [
                "Zabbix server",
                "Linux server"
            ]
        }
    },  #上一步获取的令牌'result': '198868f7543830d22a4f9845a75fd495'
    "auth": "198868f7543830d22a4f9845a75fd495", #上一步获取的令牌
    "id": 1
}
datajs = json.dumps(data)  #转成 json 格式
print(datajs,  end='---------datajs\n\n')

response = requests.post(url, headers=header, data=datajs)
print(response.json(),end = '  -----5Zabbix server\n\n') 


print('#检索主机“Zabbix server”隶属于的组名，但是不检索主机本身的详情\n\n')

data = {
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": ["hostid"],
        "selectGroups": "extend",
        "filter": {
            "host": [
                "Zabbix server"
            ]
        }
    },
    #上一步获取的令牌'result': '198868f7543830d22a4f9845a75fd495'
    "auth": "198868f7543830d22a4f9845a75fd495", #上一步获取的令牌
    "id": 2
}
datajs = json.dumps(data)  #转成 json 格式
print(datajs,  end='---------datajs\n\n')

response = requests.post(url, headers=header, data=datajs)
print(response.json(),end = '  -----6selectGroups\n\n')

#/***
#<class 'str'>
#{"jsonrpc": "2.0", "method": "user.login", "params": {"user": "admin", "password": "zabbix"}, "id": 1}---------datajs
{#'jsonrpc': '2.0', 'result': 'f3de9d7578f4167d5051727f9134724a', 'id': 1}  -----2admin
#*-**-**-**-**-**-**-**-**-**-*
#**/
##检索主机“Zabbix server”隶属于的组名，但是不检索主机本身的详情
#
#
#{"jsonrpc": "2.0", "method": "host.get", "params": {"output": ["hostid"], "selectGroups": "extend", "filter": {"host": ["Zabbix server"]}}, "auth": "198868f7543830d22a4f9845a75fd495", "id": 2}---------datajs
#
#{'jsonrpc': '2.0', 'result': [{'hostid': '10084', 'groups': [{'groupid': '4', 'name': 'Zabbix servers', 'internal': '0', 'flags': '0'}]}], 'id': 2}  -----6selectGroups
#
#https://www.zabbix.com/documentation/3.4/zh/manual/api/reference/hostgroup/get
#
#hostgroup.get
#Description 说明
#integer/array hostgroup.get(object parameters)
#The method allows to retrieve host groups according to the given parameters.
#该方法允许根据给定的参数检索主机组。
#
#Parameters 参数
#(object) Parameters defining the desired output. 
#  定义所需输出的参数。
#

##url = 'http://192.168.0.13/zabbix/api_jsonrpc.php'
##header = {'Content-Type' : 'application/json-rpc'}
#
#print('\n-----------根据给定的参数检索主机组---------------\n')
#
#data = {
#    "jsonrpc": "2.0",
#    "method": "hostgroup.get",
#    "params": {
#        "output": "extend",
##        "filter": {
##            "name": [
##                "Zabbix servers",
##                "Linux servers"
##            ]
##        }
#    },   #上一步获取的令牌{#'jsonrpc': '2.0', 'result': 'f3de9d7578f4167d5051727f9134724a', 'id': 1}  -----2admin
#    "auth": "f3de9d7578f4167d5051727f9134724a", #上一步获取的令牌'result': 'f3..
#    "id": 1
#}
#
#datajs = json.dumps(data)  #转成 json 格式
#print(datajs,  end='---------datajs\n\n')
#
#response = requests.post(url, headers=header, data=datajs)
#
#groupinfo = response.json()
#
#print(groupinfo, end = '  -----7hostgroup.get\n\n')
#
#print(groupinfo['result'], end = '  -----7groupinfo[]hostgroup.get\n\n')
#
#for  itemdict  in  groupinfo['result']:
#  print(itemdict['groupid'], itemdict['name'])
#
#



if __name__ == "__main__":
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)





