#coding=utf-8

import paramiko
import os,sys,time

blip = '10.3.45.233'
bluser = 'root'
blpasswd = 'Rfd.com'

hostname = '10.3.45.151'
username = 'tlkjadmin'
password = 'Tlkj2017c'

port = 22
passinfo="\'s password: "
paramiko.util.log_to_file('/tmp/syslogin.log')

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=blip,username=bluser,password=blpasswd)

channel = ssh.invoke_shell()
channel.settimeout(10)

buff = ''
resp = ''
channel.send('ssh '+username+'@'+hostname+'\n')
while not buff.endswith(passinfo):
    try:
        resp = channel.recv(9999)
    except Exception, e:
        print 'Error info:%s connection time.' % (str(e))
        channel.close()
        ssh.close()
        sys.exit()
    buff += resp
    if not buff.find('yes/no') == -1:
        channel.send('yes\n')
        buff=''

channel.send(password+'\n')

buff = ''

while not buff.endswith('$'):  
#while not buff.find('$'):
    resp = channel.recv(9999)
    if not resp.find(passinfo) == -1:
        print 'Error info: Authentication failed.'
        channel.close()
        ssh.close()
        sys.exit()
    buff += resp.strip()
    #buff += resp

channel.send('ifconfig\n')

buff = ''

try:
    while buff.find('$') == -1:
        resp = channel.recv(9999)
        buff += resp
except Exception, e:
    print "Error info:" + str(e)
    
print buff
channel.close()
ssh.close()