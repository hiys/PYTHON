#/usr/bin/env    python3
#coding:UTF-8
#! -*- coding:utf8 -*-
"""#coding=UTF-8
https://www.zabbix.com/documentation/3.4/zh/manual
Zabbix 手册
precondition    英 [ˌpriːkənˈdɪʃn]
    n.先决条件;前提
frontend   前端;前台;前端模块;前段;编译器前端
inventory       英 [ˈɪnvəntri]
    n.(建筑物里的物品、家具等的)清单;财产清单;(商店的)存货，库存
    v.开列清单

https://www.zabbix.com/documentation/3.4/zh/manual/api/reference/user/login
Source
CUser::login() in frontends/php/include/classes/api/services/CUser.php.
\w 匹配字母或数字或下划线_
\s 匹配任意的空白符 
\d 匹配数字    等价于[0-9]

[root@V3 zabbix]# grep  -Pnv  '^(\s*)(\*|\/|$)'   /usr/share/zabbix/include/classes/api/services/CUser.php 

[root@room9pc01 ~]# ping  -c2   192.168.0.11 >/dev/null
[root@room9pc01 ~]# tail  -2   /proc/net/arp 
192.168.0.11     0x1         0x2         52:54:00:b7:d2:89     *        vbr
192.168.1.11     0x1         0x2         52:54:00:c8:ca:e0     *        vbr1
[root@room9pc01 ~]# arp  -n   192.168.0.11
Address                  HWtype  HWaddress           Flags Mask            Iface
192.168.0.11             ether   52:54:00:b7:d2:89   C                     vbr
[root@room9pc01 ~]# arp  -n   192.168.1.11
Address                  HWtype  HWaddress           Flags Mask            Iface
192.168.1.11             ether   52:54:00:c8:ca:e0   C                     vbr1
[root@V1 ~]# ifconfig  eth0 |grep  ether
        ether 52:54:00:b7:d2:89  txqueuelen 1000  (Ethernet)
[root@V1 ~]# ifconfig  eth1 |grep  ether
        ether 52:54:00:c8:ca:e0  txqueuelen 1000  (Ethernet)

Host object 主机对象
主机对象拥有以下属性。
inventory_mode	integer	Host inventory population mode.主机资产清单群体模式
自动模式
如上清单选项卡，如果选择了自动模式，部分信息会被自动填充，
例如：主机名,系统信息。
不过其他的信息还是需要自己输入。
这个自动仅仅是把基本的信息给自动获取到，
大部分还是要自己手动补充，这顶多算个半自动模式。

https://www.zabbix.com/documentation/3.4/zh/manual/api/reference/host/object
Host inventory 主机资产清单
主机资产清单对象有以下属性。
每一个属性拥有自己唯一的ID编号，
用于将主机资产清单字段和事项关联在一起。
ID	属性	类型	说明
4	alias	string	Alias.别名
3	name	string	Name. 名称。
12	macaddress_a	string	MAC address A. MAC地址一。
13	macaddress_b	string	MAC address B. MAC地址二。
5	os	string	OS name.操作系统名称。
1	type	string	Type. 类型。
2	type_full	string	Type details. 具体类型。

zabbix agent 需要安装在被监视的目标服务器上，
它主要完成对硬件信息或与操作系统有关的内存，CPU等信息的收集。

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
#{'jsonrpc': '2.0', 'result': '4346c3a31c14a2349bbb964b782550f1', 'id': 1}  -----2admin

print('*-*' * 10, end='\n\n')
#*-**-**-**-**-**-**-**-**-**-*


print('\n-----------根据给定的参数检索主机组---------------\n\n')
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
    },   #上一步获取的令牌'result': '4346c3a31c14a2349bbb964b782550f1',
    "auth": "4346c3a31c14a2349bbb964b782550f1", #上一步获取的令牌'result': '...'
    "id": 1
}

datajs = json.dumps(data)  #转成 json 格式
print(datajs,  end='---------datajs\n\n')
#{"jsonrpc": "2.0", "method": "hostgroup.get", "params": {"output": "extend"}, "auth": "4346c3a31c14a2349bbb964b782550f1", "id": 1}---------datajs


response = requests.post(url, headers=header, data=datajs)

groupinfo = response.json()

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


print('\n\n------------- 根据指定的参数检索模板 ----------\n\n')

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
    #上一步获取的令牌'result': ''4346c3a31c14a2349bbb964b782550f1',
    "auth": "4346c3a31c14a2349bbb964b782550f1", #上一步获取的令牌'result': '...'
    "id": 1
}
datajs = json.dumps(data)  #转成 json 格式
print(datajs,  end='---------datajs\n\n')
#{"jsonrpc": "2.0", "method": "template.get", "params": {"output": "extend"}, "auth": "4346c3a31c14a2349bbb964b782550f1", "id": 1}---------datajs


response = requests.post(url, headers=header, data=datajs)

tpinfo = response.json()

for  itemdict  in   tpinfo['result']:
  print(itemdict['templateid'], itemdict['host'])

#10001 Template OS Linux
#10047 Template App Zabbix Server
#10048 Template App Zabbix Proxy
#10050 Template App Zabbix Agent
#10074 Template OS OpenBSD
#10075 Template OS FreeBSD
#10076 Template OS AIX
#10077 Template OS HP-UX
#10078 Template OS Solaris
#10079 Template OS Mac OS X
#10081 Template OS Windows
#10093 Template App FTP Service
#10094 Template App HTTP Service
#10095 Template App HTTPS Service
#10096 Template App IMAP Service
#10097 Template App LDAP Service
#10098 Template App NNTP Service
#10099 Template App NTP Service
#10100 Template App POP Service
#10101 Template App SMTP Service
#10102 Template App SSH Service
#10103 Template App Telnet Service
#10168 Template App Apache Tomcat JMX
#10169 Template App Generic Java JMX
#10170 Template DB MySQL
#10171 Template Server Intel SR1530 IPMI
#10172 Template Server Intel SR1630 IPMI
#10173 Template VM VMware
#10174 Template VM VMware Guest
#10175 Template VM VMware Hypervisor
#10182 Template Module EtherLike-MIB SNMPv1
#10183 Template Module EtherLike-MIB SNMPv2
#10184 Template Module HOST-RESOURCES-MIB SNMPv1
#10185 Template Module HOST-RESOURCES-MIB SNMPv2
#10186 Template Module ICMP Ping
#10187 Template Module Interfaces Simple SNMPv1
#10188 Template Module Interfaces Simple SNMPv2
#10189 Template Module Interfaces SNMPv1
#10190 Template Module Interfaces SNMPv2
#10192 Template Module Interfaces Windows SNMPv2
#10203 Template Module Generic SNMPv1
#10204 Template Module Generic SNMPv2
#10207 Template Net Alcatel Timetra TiMOS SNMPv2
#10208 Template Net Brocade FC SNMPv2
#10209 Template Module Brocade_Foundry Performance SNMPv2
#10210 Template Net Brocade_Foundry Nonstackable SNMPv2
#10211 Template Net Brocade_Foundry Stackable SNMPv2
#10212 Template Module Cisco CISCO-MEMORY-POOL-MIB SNMPv2
#10213 Template Module Cisco CISCO-PROCESS-MIB SNMPv2
#10215 Template Module Cisco OLD-CISCO-CPU-MIB SNMPv2
#10216 Template Module Cisco Inventory SNMPv2
#10217 Template Module Cisco CISCO-ENVMON-MIB SNMPv2
#10218 Template Net Cisco IOS SNMPv2
#10220 Template Net Cisco IOS prior to 12.0_3_T SNMPv2
#10221 Template Net Dell Force S-Series SNMPv2
#10222 Template Net D-Link DES 7200 SNMPv2
#10223 Template Net D-Link DES_DGS Switch SNMPv2
#10224 Template Net Extreme EXOS SNMPv2
#10225 Template Net Network Generic Device SNMPv1
#10226 Template Net Network Generic Device SNMPv2
#10227 Template Net HP Comware HH3C SNMPv2
#10229 Template Net Huawei VRP SNMPv2
#10230 Template Net Intel_Qlogic Infiniband SNMPv2
#10231 Template Net Juniper SNMPv2
#10233 Template Net Mikrotik SNMPv2
#10234 Template Net Netgear Fastpath SNMPv2
#10235 Template Net QTech QSW SNMPv2
#10236 Template Net TP-LINK SNMPv2
#10237 Template Net Ubiquiti AirOS SNMPv1
#10248 Template OS Linux SNMPv2
#10249 Template OS Windows SNMPv2
#10250 Template Net HP Enterprise Switch SNMPv2
#10251 Template Net Mellanox SNMPv2
#10252 Template Module Cisco CISCO-PROCESS-MIB IOS versions 12.0_3_T-12.2_3.5 SNMPv2
#10253 Template Net Cisco IOS versions 12.0_3_T-12.2_3.5 SNMPv2


#https://www.zabbix.com/documentation/3.4/zh/manual/api/reference/host/create
#Source 来源
#CHost::create() in frontends/php/include/classes/api/services/CHost.php.
#18. Web界面
#19. API
#方法参考
#Action 动作
#API 信息
#Correlation 关联
#Graph item图形项
#Graph prototype 原型图
#Graph 图形
#Host interface 主机接口 #点击连接
#Host prototype 主机原型
#Icon map 图标拓扑图
#Item prototype Item原型

#Host interface 主机接口
#> Host interface object主机接口对象#点击链接
#hostinterface.create
#hostinterface.delete
#hostinterface.get #点击链接
#https://www.zabbix.com/documentation/3.4/zh/manual/api/reference/hostinterface/get
#https://www.zabbix.com/documentation/3.4/zh/manual/api/reference/hostinterface/object
#参数	类型	描述
#interfaceid	string	(readonly) ID of the interface.接口的ID。
#dns 
#(required)	string	DNS name used by the interface.接口使用的DNS名称。 
#Can be empty if the connection is made via IP.如果通过IP进行连接，则可以为空。

#[root@V3 zabbix]# ll   /usr/share/zabbix/include/classes/api/services/CHost.php 
#-rw-r--r--. 1 root root 65233 11月 12 18:50 /usr/share/zabbix/include/classes/api/services/CHost.php
print('\n\n-------- 创建一个具有IP接口的Linux Server 主机，将其添加到主机组中，链接一个模板并且把MAC地址设置到主机资产清单里  ----------\n\n')
print('#2 Linux servers主机组 ----- #10001 Template OS Linux模板\n')
print('---创建名为myLinux1的主机，它在Linux servers组中，应用Template OS Linux模板----\n\n')

data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "myLinux1",
        "interfaces": [
            {
                "type": 1, #1 agent,采用zabbix agent方式监控; 2SNMP接口;3IPMI接口;4JMX接口
                "main": 1, #0 非默认接口;1该接口在主机上用作默认接口
                "useip": 1,#0使用主机DNS域名hostname; 1 使用主机接口的ip地址连接
                "ip": "192.168.0.11", #接口连接的ip地址,myLinux的主机ip
                "dns": "V1",   #接口使用的DNS名称,若通过IP进行连接，则可以为空""
                "port": "10050"
            }
        ],
        "groups": [
            {
                "groupid": "2"   #2 Linux servers主机组
            }
        ],
        "templates": [
            {
                "templateid": "10001"  ##10001 Template OS Linux模板
            }
        ],              # -1 已禁用;0(默认)手动模式； 1 - automatic自动模式
        "inventory_mode": 0,  # 主机资产记录,主机资产清单群体模式0(默认)手动模式；
        "inventory": {
            "macaddress_a": "52:54:00:b7:d2:89", #输入当前设备的mac地址MAC地址一:Mac地址A
            "macaddress_b": "52:54:00:c8:ca:e0"  #MAC地址二:Mac地址B
        }
    },
    #上一步获取的令牌'result': ''4346c3a31c14a2349bbb964b782550f1',
    "auth": "4346c3a31c14a2349bbb964b782550f1", #上一步获取的令牌'result': '...'
    "id": 1
}
datajs = json.dumps(data)  #转成 json 格式
print(datajs,  end='---------datajs\n\n')
#{"jsonrpc": "2.0", "method": "host.create", "params": {"host": "myLinux1", "interfaces": [{"type": 1, "main": 1, "useip": 1, "ip": "192.168.0.11", "dns": "V1", "port": "10050"}], "groups": [{"groupid": "2"}], "templates": [{"templateid": "10001"}], "inventory_mode": 0, "inventory": {"macaddress_a": "52:54:00:b7:d2:89", "macaddress_b": "52:54:00:c8:ca:e0"}}, "auth": "4346c3a31c14a2349bbb964b782550f1", "id": 1}---------datajs

response = requests.post(url, headers=header, data=datajs)

info = response.json()
print('\n--------info ---------\n%s ---END\n' % info )
#--------info ---------
#{'jsonrpc': '2.0', 'result': {'hostids': ['10254']}, 'id': 1} ---END





if __name__ == "__main__":
  sys.stdout.write('\033[31;47;1msys.argv is %s\n\033[0m' % sys.argv)






