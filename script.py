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

def subprocess_cmd(command):
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    return proc_stdout

r = expon.rvs(scale=2,size=50,random_state=2)
a = 0

FNULL = open(os.devnull, 'w')

with open(sys.argv[1],'r') as queries:
	for line in queries:
		proc = subprocess.Popen(['taskset','0x3','google-chrome','--load-extension=/home/indrajeet/Downloads/Content','--new-window ',line], shell=False, stdout=FNULL, stderr=subprocess.STDOUT)
		temp_pids = subprocess_cmd("ps -eo pid,comm | awk '$2~/chrome/ {print $1}'")
		print temp_pids
		time.sleep(r[a])
		a = a+1

