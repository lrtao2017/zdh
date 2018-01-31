#coding=utf-8

import pexpect
import sys

ip = "127.0.0.1"
user = "root"
passwd = "123456"
target_file = "prometheus.log"

child = pexpect.spawn('/usr/bin/ssh',[user+'@'+ip])
fout = file("mylog_02.txt",'w')
child.logfile = fout
#child.logfile = sys.stdout

try:
    child.expect('(?i)password:')
    child.sendline(passwd)
    child.expect('#')
    child.sendline('cd /tmp')
    child.expect('#')
    child.sendline('/bin/tar -czf prometheus.log.tar.gz '+target_file)
    
    child.expect('#')
    print child.before
    child.sendline('exit')
    fout.close()
except pexpect.exceptions.EOF as EOF:
    print "expect EOF"
    
except pexpect.exceptions.TIMEOUT as TIMEOUT:
    print "expect TIMEOUT"
    
child = pexpect.spawn('/usr/bin/scp',[user+'@'+ip+':/tmp/prometheus.log.tar.gz','/tmp'])
fout = file("mylog_02.txt",'a')
child.logfile = fout
#child.logfile = sys.stdout

try:
    child.expect('(?i)password:')
    child.sendline(passwd)
    child.expect(pexpect.EOF)
except pexpect.exceptions.EOF as EOF:
    print "expect EOF"
except pexpect.exceptions.TIMEOUT as TIMEOUT:
    print "expect TIMEOUT"
