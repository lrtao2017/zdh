#coding=utf-8

import paramiko
import os,sys,time

blip = '127.0.0.1'
bluser = 'root'
blpasswd = '123456'

hostname = '127.0.0.1'
username = 'root'
password = '123456'

tmpdir = '/tmp'
remotedir = '/tmp'
localpath = '/tmp/syslogin.log'
tmppath = tmpdir+r'/syslogin.log'
remotepath = remotedir+r'/syslogin.log'

port = 22
passinfo="\'s password: "
paramiko.util.log_to_file('/tmp/syslogin.log')

t = paramiko.Transport((blip, port))
t.connect(username= bluser, password = blpasswd)
sftp = paramiko.SFTPClient.from_transport(t)
sftp.put(localpath,tmppath)
sftp.close()

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=blip,username=bluser,password=blpasswd)

channel = ssh.invoke_shell()
channel.settimeout(10)

buff = ''
resp = ''
channel.send('scp '+tmppath+' '+username+'@'+hostname+':'+remotepath+'\n')
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
while not buff.endswith('#'):  
#while not buff.find('$'):
    resp = channel.recv(9999)
    print resp
    if not resp.find(passinfo) == -1:
        print 'Error info: Authentication failed.'
        channel.close()
        ssh.close()
        sys.exit()
    buff += resp.strip()
    #buff += resp
    
print buff
channel.close()
ssh.close()
