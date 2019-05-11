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


https://www.zabbix.com/documentation/3.4/zh/manual/api/reference/template/get
template.get

Description说明
integer/array template.get(object parameters)
The method allows to retrieve templates according to the given parameters
该方法允许根据指定的参数检索模板.

Parameters参数
(object) Parameters defining the desired output
定义所需输出的参数.
The method supports the following parameters
该方法支持以下参数.

Parameter参数	Type类型	Description说明
templateids	string/array	Return only templates with the given template IDs只返回具有给定模板ID的模板.

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


response = requests.post(url, headers=header, data=datajs)
print(response.json(),end = '  -----1apiinfo.version\n')    #zabbix返回 json格式的数据

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
print(type(datajs), datajs, sep='\n', end='---------datajs\n\n')

response = requests.post(url, headers=header, data=datajs)
print(response.json(),end = '  -----2admin\n')    #zabbix返回 json格式的数据

#<class 'str'>
#{"jsonrpc": "2.0", "method": "user.login", "params": {"user": "admin", "password": "zabbix"}, "id": 1}---------datajs
#
#{'jsonrpc': '2.0', 'result': '021f5a16485203b03a956b3c0891b66c', 'id': 1}  -----2admin

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
print(type(datajs), datajs, sep='\n', end='---------datajs\n\n')

response = requests.post(url, headers=header, data=datajs)
print(response.json(),end = '  -----3root\n')    #zabbix返回 json格式的数据


print('$-$' * 10, end='\n\n')




url = 'http://192.168.0.13/zabbix/api_jsonrpc.php'
header = {'Content-Type' : 'application/json-rpc'}

print('\n-----------根据给定的参数检索主机组---------------\n')
#-----------根据给定的参数检索主机组---------------

data = {
    "jsonrpc": "2.0",
    "method": "hostgroup.get",
    "params": {
        "output": "extend",
#        "filter": {
#            "name": [
#                "Zabbix servers",
#                "Linux servers"
#            ]
#        }
    },   #上一步获取的令牌'result': '021f5a16485203b03a956b3c0891b66c',
    "auth": "021f5a16485203b03a956b3c0891b66c", #上一步获取的令牌'result': '...'
    "id": 1
}

datajs = json.dumps(data)  #转成 json 格式
print(datajs,  end='---------datajs\n\n')
#{"jsonrpc": "2.0", "method": "hostgroup.get", "params": {"output": "extend"}, "auth": "021f5a16485203b03a956b3c0891b66c", "id": 1}---------datajs

response = requests.post(url, headers=header, data=datajs)

groupinfo = response.json()

#print(groupinfo, end = '  -----7hostgroup.get\n\n')
#{'jsonrpc': '2.0', 'result': [{'groupid': '1', 'name': 'Templates', 'internal': '0', 'flags': '0'}, {'groupid': '2', 'name': 'Linux servers', 'internal': '0', 'flags': '0'}, {'groupid': '4', 'name': 'Zabbix servers', 'internal': '0', 'flags': '0'}, {'groupid': '5', 'name': 'Discovered hosts', 'internal': '1', 'flags': '0'}, {'groupid': '6', 'name': 'Virtual machines', 'internal': '0', 'flags': '0'}, {'groupid': '7', 'name': 'Hypervisors', 'internal': '0', 'flags': '0'}, {'groupid': '8', 'name': 'Templates/Modules', 'internal': '0', 'flags': '0'}, {'groupid': '9', 'name': 'Templates/Network Devices', 'internal': '0', 'flags': '0'}, {'groupid': '10', 'name': 'Templates/Operating Systems', 'internal': '0', 'flags': '0'}, {'groupid': '11', 'name': 'Templates/Servers Hardware', 'internal': '0', 'flags': '0'}, {'groupid': '12', 'name': 'Templates/Applications', 'internal': '0', 'flags': '0'}, {'groupid': '13', 'name': 'Templates/Databases', 'internal': '0', 'flags': '0'}, {'groupid': '14', 'name': 'Templates/Virtualization', 'internal': '0', 'flags': '0'}], 'id': 1}  -----7hostgroup.get


#print(groupinfo['result'], end = '  -----7groupinfo[]hostgroup.get\n\n')
#[{'groupid': '1', 'name': 'Templates', 'internal': '0', 'flags': '0'}, {'groupid': '2', 'name': 'Linux servers', 'internal': '0', 'flags': '0'}, {'groupid': '4', 'name': 'Zabbix servers', 'internal': '0', 'flags': '0'}, {'groupid': '5', 'name': 'Discovered hosts', 'internal': '1', 'flags': '0'}, {'groupid': '6', 'name': 'Virtual machines', 'internal': '0', 'flags': '0'}, {'groupid': '7', 'name': 'Hypervisors', 'internal': '0', 'flags': '0'}, {'groupid': '8', 'name': 'Templates/Modules', 'internal': '0', 'flags': '0'}, {'groupid': '9', 'name': 'Templates/Network Devices', 'internal': '0', 'flags': '0'}, {'groupid': '10', 'name': 'Templates/Operating Systems', 'internal': '0', 'flags': '0'}, {'groupid': '11', 'name': 'Templates/Servers Hardware', 'internal': '0', 'flags': '0'}, {'groupid': '12', 'name': 'Templates/Applications', 'internal': '0', 'flags': '0'}, {'groupid': '13', 'name': 'Templates/Databases', 'internal': '0', 'flags': '0'}, {'groupid': '14', 'name': 'Templates/Virtualization', 'internal': '0', 'flags': '0'}]  -----7groupinfo[]hostgroup.get


for  itemdict  in  groupinfo['result']:
  print(itemdict['groupid'], itemdict['name'])
#1 Templates
#2 Linux servers
#4 Zabbix servers
#5 Discovered hosts
#6 Virtual machines
#7 Hypervisors
#8 Templates/Modules
#9 Templates/Network Devices
#10 Templates/Operating Systems
#11 Templates/Servers Hardware
#12 Templates/Applications
#13 Templates/Databases
#14 Templates/Virtualization
#


print('\n------------- 根据指定的参数检索模板 ----------\n\n')

data = {
    "jsonrpc": "2.0",
    "method": "template.get",
    "params": {
        "output": "extend",
#        "filter": {
#            "host": [
#                "Template OS Linux",
#                "Template OS Windows"
#            ]
#        }
    },
    #上一步获取的令牌'result': '021f5a16485203b03a956b3c0891b66c',
    "auth": "021f5a16485203b03a956b3c0891b66c", #上一步获取的令牌'result':'...'
    "id": 1
}
datajs = json.dumps(data)  #转成 json 格式
#print(datajs,  end='---------datajs\n\n')


response = requests.post(url, headers=header, data=datajs)

tpinfo = response.json()
#print(tpinfo, end = '  -----template.get\n\n')

for  itemdict  in   tpinfo['result']:
  print(itemdict['templateid'], itemdict['host'])





if __name__ == "__main__":
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)



