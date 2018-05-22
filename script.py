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

timesnow_actual = []
energy_actual = []
#sum_timesnow_actual = sum(timesnow_actual)
#sum_energy_actual = sum(energy_actual)

abc = 0
def printit():
	if (abc==1):
		return
	threading.Timer(5.0,printit).start()
	cmd = "perf stat -a -r 1 -e power/energy-pkg/ sleep 5"
	p = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out,err = p.communicate()
	timesnow = err.split('\n')[5]
	energy = err.split('\n')[3]
	timesnow_actual.append(float(timesnow.split()[0]))
	energy_actual.append(float(energy.split()[0]))
	print 'Total time elapsed : ',sum(timesnow_actual)
	print 'Total Joules consumed : ',sum(energy_actual)

printit()

def subprocess_cmd(command):
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    return proc_stdout

r = expon.rvs(scale=5,size=50,random_state=2)
a = 0

FNULL = open(os.devnull, 'w')
sprinted_pids = [];

with open(sys.argv[1],'r') as queries:
	for line in queries:
		proc = subprocess.Popen(['taskset','0x1','google-chrome','--load-extension=/home/indrajeet/Downloads/Content','--new-window ',line], shell=False, stdout=FNULL, stderr=subprocess.STDOUT)
		temp_pids = subprocess_cmd("ps -eo pid,etimes,comm | awk '$3~/chrome/ {print $1}'")
		temp_etimes = subprocess_cmd("ps -eo pid,etimes,comm | awk '$3~/chrome/ {print $2}'")
		temp_pids_int = [int(s) for s in temp_pids.split('\n')]
		temp_etimes_int = [int(s) for s in temp_etimes.split('\n')]
		for idx,etime in enumerate(temp_etimes_int[10:]):
			if etime>1 and temp_pids_int[10+idx] not in sprinted_pids:
				print "------"
				proc2 = subprocess.Popen(['taskset','-p','0xF',str(temp_pids_int[10+idx])])
				sprinted_pids.append(temp_pids_int[10+idx])
				#print sprinted_pids
			if etime>30:
				proc1 = subprocess.Popen(['kill','-15',str(temp_pids_int[10+idx])])
				print "Just Killed",temp_pids_int[10+idx],"!!!"

		time.sleep(r[a])
		a = a+1
abc = 1

# keep note of power energy and dont exceed budget
#timeout to sprint varies from 10,15,20,etc...,
#change number of cores without sprinting and with sprinting give 1,2,3 more cores respectively
#web of things confernce 
#num of times you are loading 50 web pages
#when it crashes have a mechanism to start wheere you left
#get the excel sheets

