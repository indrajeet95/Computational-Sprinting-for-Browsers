#!/usr/bin/python

import subprocess
import time
import datetime
import sys
import os
import signal
import psutil

#ts = time.time()
#print ts
#st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
#print st

#pids = [];
#times = [];
#my_dict = {};
#a = 1;
FNULL = open(os.devnull,'w')
with open(sys.argv[1],'r') as queries:
	for line in queries:
		retcode = subprocess.call(['taskset','0x3','google-chrome','--load-extension=/home/indrajeet/Downloads/Content','--new-window ',line],stdout=FNULL,stderr=subprocess.STDOUT)

#		command = "taskset 0x3 google-chrome --load-extension=/home/indrajeet/Downloads/Content --new-window %s &> /dev/null" % (line)
# taskset 0x3 google-chrome --enable-logging=stderr --v=1 --load-extension=/home/indrajeet/Downloads/Content --new-window "$line" &>/dev/null &
#		process = subprocess.Popen(['taskset','0x3','google-chrome','--v=1','--load-extension=/home/indrajeet/Downloads/Content','--new-window ',line])
#		p = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE)
		#print p
#		output = subprocess.Popen(['taskset','0x3','google-chrome','--enable-logging=stderr','--v=1','--load-extension=/home/indrajeet/Downloads/Content','&>/dev/null','&','echo $!','--new-window',line], stdout=subprocess.PIPE).communicate()[0]
		#print p
#		my_dict[process.pid] = a
#		a += 1
#		pids.append([process.pid,time.time()])
#		blist.append(time.time())
#		print pids
		#print ts
#		print times
#		print my_dict
#		for pid in pids[3:]:
#			print time.time() - pid[1]
#			if time.time() - pid[1] > 30:
#				output = subprocess.Popen(['kill','-15 ',pid[0])
#				p = psutil.Process(pid[0])
#				p.terminate()
#				
#				print pid[0]
#				os.kill(pid[0],signal.SIGKILL)	
#for the pid in pids starting from range 10 if time > 30, subprocess. kill pid
#			if(pids.times
		time.sleep(5)


#exponential arrival time
#implement sprinting at constant threshold like 15, 20, 25 seconds.
#implement killing process if it takes more than certain time


