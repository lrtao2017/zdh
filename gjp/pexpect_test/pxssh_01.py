#coding=utf-8

from pexpect import pxssh
import getpass

try:
    s = pxssh.pxssh()
    hostname = raw_input("hostname:")
    username = raw_input("username:")
    password = getpass.getpass('please input password:')
    s.login (hostname, username, password)
    s.sendline ('uptime')
    s.prompt()
    print s.before
    s.sendline ('ls -l')
    s.prompt()
    print s.before
    s.sendline ('df -lh')
    s.prompt()
    print s.before
    s.logout()
except pxssh.ExceptionPxssh,e:
    print "pxssh failed on login."
    print str(e)
    
    
    
    
    
    
    
    

