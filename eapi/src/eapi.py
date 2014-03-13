# coding=utf-8
from jsonrpclib import Server
#import json

# 장비 접속
switch = Server ( "http://admin:@gkstjs@14.63.250.195:7211/command-api" )

#~~~~~~~~~RRRRRR


def desc_range():
    response = switch.runCmds( 1, [ "enable" ,
                                    "show interfaces description" ] ,
                                    "text")
    print response    
#desc_range()


def run_int(n):
    response = switch.runCmds( 1, [ "enable" ,
                                    "show running-config interfaces ethernet "+str(n) ] ,
                                    "text")
    s = str(response)
    if 'shutdown' in s:
        print 'interface ethernet '+str(n)+' : shutdown'
    else:
        print 'interface ethernet '+str(n)+' no shutdown'
      
#run_int(1)

#
def addvlan(v,w,su):
    response = switch.runCmds( 1, [ "enable" ,
                                    "configure terminal",
                                    "interface vlan "+v,
                                    "description "+v+" cccclient",
                                    "ip address "+w+" "+su ] ,
                                    "json")
    print response
#s
addvlan("3007","14.63.251.2","255.255.255.0")


def acl(v,w,su):
    response = switch.runCmds( 1, [ "enable" ,
                                    "configure terminal",
                                    "interface vlan "+v,
                                    "description "+v+" cccclient",
                                    "ip address "+w+" "+su ] ,
                                    "json")
    print response

#acl("3007","14.63.251.2","255.255.255.0")












'''
    for x in range(1, 3):
        response = switch.runCmds( 1, [
                                    "enable" ,
                                    "configure" ,
                                    "interface ethernet" + str(x) ,
                                    "description TOR uuuuuuuu-" + str(x) ] ,
                                    "json")
        print "interface ethernet " + str(x) +" done"
'''   

'''
response = switch.runCmds( 1, [ "show version" ] )
                   
print json.dumps(response,  sort_keys = True, 
                                     indent = 4, 
                                    separators=(',', ': '))

print response
'''




