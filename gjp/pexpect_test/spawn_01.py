#coding=utf-8

import pexpect
import sys

ip = "127.0.0.1"
user = "root"
passwd = "123456"
target_file = "/root/install.log"

child = pexpect.spawn('ssh',[user+'@'+ip])
fout = file("mylog_02.txt",'w')
child.logfile = fout

try:
    child.expect('(?i)password')
    child.sendline(passwd)
    child.expect('#')
    child.sendline('tar -czf /root/install.log.tar.gz'+target_file)
    
    child.expect('#')
    print child.before
    child.sendline('exit')
    fout.close()
except EOF:
    print "expect EOF"
    
except TIMEOUT:
    print "expect TIMEOUT"
    
child = pexpect.spawn('scp',[user+'@'+ip+':/root/install.log.tar.gz','/tmp'])
fout = file("mylog_02.txt",'a')
child.logfile = fout

try:
    child.expect('(?i)password')
    child.sendline(passwd)
    child.expect(pexpect.EOF)
except EOF:
    print "expect EOF"
except TIMEOUT:
    print "expect TIMEOUT"
