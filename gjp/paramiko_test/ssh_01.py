#coding=utf-8

import paramiko

hostname = '127.0.0.1'
username = 'root'
password = '123456'
paramiko.util.log_to_file('syslogin.log')

ssh = paramiko.SSHClient()
#ssh.load_system_host_keys()
#ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.set_missing_host_key_policy(paramiko.WarningPolicy())


ssh.connect(hostname=hostname,username=username,password=password)
stdin,stdout,stderr=ssh.exec_command('free -m')
print "free -m"
print stdout.read()
stdin,stdout,stderr=ssh.exec_command('df -lh')
print "df -lh"
print stdout.read()
ssh.close()