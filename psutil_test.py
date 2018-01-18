#coding=utf-8
'''
retrieving information on running processes 
and system utilization (CPU, memory, disks, 
network, sensors
'''

import psutil

mem = psutil.virtual_memory()
mem_total = mem.total / 1024 / 1024 
mem_used = mem.used / 1024 / 1024

cpu_user = psutil.cpu_times().user
cpu_user_percent = psutil.cpu_times_percent().user
cpu_count = psutil.cpu_count()

sda1_read_count = psutil.disk_io_counters(perdisk=True).get("sda1").read_count
disk_used_percent = psutil.disk_usage('/').percent

eth0_sent = psutil.net_io_counters(pernic=True).get('eth0').bytes_sent/1024/1024
eth0_recv = psutil.net_io_counters(pernic=True).get('eth0').bytes_recv/1024/1024
print "information of Memory:"
print "total(M) %15s " % mem_total
print "used(M) %15s " % mem_used
print '\n'
print "information of Cpu"
print "user %20s" % cpu_user
print "user_percent %10s" % cpu_user_percent
print "count %15s" % cpu_count
print '\n'
print "information of Disk"
print "used_percent %13s" % disk_used_percent
print "disk_read_count %10s" % sda1_read_count
print '\n'
print "information of Network"
print "eth0_sent(M) %13s" % eth0_sent
print "eth0_recv(M) %13s" % eth0_recv
