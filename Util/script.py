#!/usr/bin/python

import subprocess
import time
import datetime
import sys
import os
import signal
import psutil
from scipy.stats import expon
import matplotlib.pyplot as plt
import threading

webpages = sys.argv[1]
energy_budget = sys.argv[2]
sprint_timeout = sys.argv[3]
kill_timeout = sys.argv[4]
inter_arrival_scale = sys.argv[5]
base_cores = sys.argv[6]
sprint_cores = sys.argv[7]
#base_cores, sprint_cores = '0x1','0x3','0x7','0xf'

file_name = energy_budget + '_' + sprint_timeout + '_' + kill_timeout + '_' + inter_arrival_scale + '_' + base_cores + '_' + sprint_cores
f = open('%s.txt'% file_name,'wb')

flag = 0
timesnow_actual = []
energy_actual = []

def printit():
	if (flag==1):
		return
	threading.Timer(1.0,printit).start()
	cmd = "perf stat -a -r 1 -e power/energy-pkg/ sleep 1"
	p = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out,err = p.communicate()
	timesnow = err.split('\n')[5]
	energy = err.split('\n')[3]
	timesnow_actual.append(float(timesnow.split()[0]))
	energy_actual.append(float(energy.split()[0]))
	f.write("\nTotal time elapsed : %s\n" % sum(timesnow_actual))
	f.write("Total Joules consumed : %s\n" % sum(energy_actual))

printit()

def subprocess_cmd(command):
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    return proc_stdout

r = expon.rvs(scale=float(inter_arrival_scale),size=100,random_state=10)
a = 0

FNULL = open(os.devnull, 'w')
sprinted_pids = []

with open(webpages,'r') as queries:
	for line in queries:
		proc = subprocess.Popen(['taskset',base_cores,'google-chrome','--load-extension=/home/indrajeet/Downloads/Content','--new-window ',line], shell=False, stdout=FNULL, stderr=subprocess.STDOUT)
		pids = subprocess_cmd("ps -eo pid,etimes,comm | awk '$3~/chrome/ {print $1}'")
		etimes = subprocess_cmd("ps -eo pid,etimes,comm | awk '$3~/chrome/ {print $2}'")
		pids_int = [int(s) for s in pids.split('\n')]
		etimes_float = [float(s) for s in etimes.split('\n')]
		for idx,etime in enumerate(etimes_float[15:]):
			try:
				if etime>float(sprint_timeout) and sum(energy_actual) < float(energy_budget) and pids_int[15+idx] not in sprinted_pids:
					proc2 = subprocess.Popen(['taskset','-p',sprint_cores,str(pids_int[15+idx])],stdout=f)
					sprinted_pids.append(pids_int[15+idx])
			except IndexError:
				f.write("\nIndex Error\n")
		for idx,etime in enumerate(etimes_float[15:]):
			if etime>float(kill_timeout):
				try:
					proc1 = subprocess.Popen(['kill','-15',str(pids_int[15+idx])])
					#f.write("\nJust Killed %s !!!\n" % pids_int[10+idx])
				except IndexError:
					f.write("\nIndex Error\n")
		time.sleep(r[a])
		a = a+1
flag = 1

time.sleep(60)
for pid in pids_int:
	proc_last = subprocess.Popen(['kill','-9',str(pid)])

print "KILLED ALL CHROME PROCESSES. Time to start the next run....."

# when it crashes have a mechanism to start where you left NOT YET
