#coding=utf-8

import pexpect
import sys

child = pexpect.spawn('ssh root@127.0.0.1')
#fout = file('mylog_01.txt','w')
#child.logfile = fout

child.logfile = sys.stdout

child.expect("password:")
child.sendline("123456")
child.expect("#")
child.sendline('ls /home')
child.expect("#")