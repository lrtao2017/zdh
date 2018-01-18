#coding=utf-8
'''
retrieving information on running processes 
'''

import psutil
import os
import datetime

#PID = psutil.pids()

p_own = psutil.Process(os.getpid())

print p_own.name() 
print p_own.exe()
print p_own.cwd()
print datetime.datetime.fromtimestamp(p_own.create_time()).strftime("%Y-%m-%d %H:%M:%S")
print p_own.status()
print p_own.uids()
print p_own.gids()
print p_own.cpu_times()
print p_own.cpu_affinity()
print p_own.memory_percent()
print p_own.io_counters()
print p_own.connections()
print p_own.num_threads()
