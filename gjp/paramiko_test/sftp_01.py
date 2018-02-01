#coding=utf-8

import paramiko

username = 'root'
password = '123456'
hostname = '127.0.0.1'
port = 22

try:
    t = paramiko.Transport((hostname,port))
    t.connect(username=username,password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    
    sftp.put('/tmp/install.log.tar.gz','/tmp/install_01.log.tar.gz')
    sftp.get('/tmp/prometheus.log','/tmp/prometheus_01.log')
    sftp.mkdir('/tmp/test',0755)
    sftp.rmdir('/tmp/test01')
    sftp.rename('/tmp/prometheus.log','/tmp/prometheus_newname.log')
    print sftp.stat('/tmp/prometheus.log.tar.gz')
    print sftp.listdir('/tmp')
    t.close()
    
except Exception, e:
    print str(e)
    
