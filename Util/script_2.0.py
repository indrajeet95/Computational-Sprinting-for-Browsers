#!/usr/bin/python

import re
import csv
import subprocess
import time
from datetime import datetime
import sys
import os
import signal
import psutil
from scipy.stats import expon
import matplotlib.pyplot as plt
import threading
import mysql.connector

config = {
	'user': 'root',
	'password': 'root',
	'host': 'localhost',
	'database': 'mydb',
	'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)

webpages = sys.argv[1]
energy_budget = sys.argv[2]
sprint_timeout = sys.argv[3]
kill_timeout = sys.argv[4]
inter_arrival_scale = sys.argv[5]
base_cores = sys.argv[6]
sprint_cores = sys.argv[7]
no_of_pages_file_name = sys.argv[1].split('/')[6]
no_of_pages = int(no_of_pages_file_name.split('_')[0])

file_name = energy_budget + '_' + sprint_timeout + '_' + kill_timeout + '_' + inter_arrival_scale + '_' + base_cores + '_' + sprint_cores
f = open('%s.txt'% file_name,'w+')

flag = 0
timesnow_actual = []
energy_actual = []

def subprocess_cmd(command):
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    return proc_stdout

#Error timesnow.split()[0] index out of range... -> perf command not working
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
	f.write("\n%s Net. time elapsed : %s\n" %(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), sum(timesnow_actual)))
	f.write("%s Net. Joules consumed : %s\n" %(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), sum(energy_actual)))

printit()

def kill():
	if(flag == 1):
		return
	threading.Timer(0.1,kill).start()
	pids = subprocess_cmd("ps -eo pid,etimes,comm | awk '$3~/chrome/ {print $1}'")
	etimes = subprocess_cmd("ps -eo pid,etimes,comm | awk '$3~/chrome/ {print $2}'")
	if len(pids) != 0 and len(etimes) != 0:
		pids_list = [s for s in pids.split('\n')]
		etimes_list = [int(s) for s in etimes.split('\n')]
		for idx,etime in enumerate(etimes_list[10:]):
			if etime > int(kill_timeout):
				try:
					proc1 = subprocess.Popen(['kill','-9',str(pids_list[10+idx])])
					f.write("\n%s Just Killed %s !!!\n" %(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), str(pids_list[10+idx])))
				except IndexError:
					f.write("\n%s Index Error\n" %(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

kill()

sprinted_pids = []

def sprint():
	if(flag == 1):
		return
	threading.Timer(0.1,sprint).start()
	pids = subprocess_cmd("ps -eo pid,etimes,comm | awk '$3~/chrome/ {print $1}'")
	etimes = subprocess_cmd("ps -eo pid,etimes,comm | awk '$3~/chrome/ {print $2}'")
	if len(pids) != 0 and len(etimes) != 0:
		pids_list = [s for s in pids.split('\n')]
		etimes_list = [int(s) for s in etimes.split('\n')]
		for idx,etime in enumerate(etimes_list[10:]):
			try:
				if etime > int(sprint_timeout) and sum(energy_actual) < float(energy_budget) and str(pids_list[10+idx]) not in sprinted_pids:
					try:
						proc2 = subprocess.Popen(['taskset','-p',sprint_cores,str(pids_list[10+idx])],stdout=f,stderr=f)
						sprinted_pids.append(str(pids_list[10+idx]))
					except IndexError:
						f.write("\n%s Index Error\n" %(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
			except IndexError:
				f.write("\n%s Index Error\n" %(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
sprint()

r = expon.rvs(scale=float(inter_arrival_scale),size=no_of_pages,random_state=10)
a = 0

FNULL = open(os.devnull, 'w')

with open(webpages,'r') as queries:
	for line in queries:
		proc = subprocess.Popen(['taskset',base_cores,'google-chrome','--load-extension=/home/indrajeet/Desktop/Computational-Sprinting-for-Browsers/Content','--new-window ',line], shell=False, stdout=FNULL, stderr=subprocess.STDOUT)
		time.sleep(r[a])
		a = a+1

time.sleep(30)
flag = 1

pids_global = subprocess_cmd("ps -eo pid,etimes,comm | awk '$3~/chrome/ {print $1}'")
pids_list_global = [s for s in pids_global.split('\n')]
for pid in pids_list_global:
	proc_last = subprocess.Popen(['kill','-9',str(pid)])

print "KILLED ALL CHROME PROCESSES. Time to start the next run....."
#Time to get the exact energy consumption using the timestamp from the database and matching it on the results that we just collected and write the data on on excel sheet"

cursor = cnx.cursor()
csv_writer = csv.writer(open('%s.csv' %file_name,'wb'))
cursor.execute("SELECT * FROM data")
for row in cursor.fetchall():
	csv_writer.writerow(row)

cursor.execute("SELECT * FROM data ORDER BY id DESC LIMIT 1")
last_row = cursor.fetchone()
print last_row
timestamp_last_row = last_row[1]

str_match = str(timestamp_last_row) + ' Net. Joules'
print str_match

f_again = open('%s.txt'% file_name,'r+')
for line in f_again:
	if re.match(str_match,line):
		word_list = line.split()
		f.write("\nNET JOULES CONSUMED: %s\n" %word_list[-1])

cursor.execute("TRUNCATE TABLE data")
cnx.close()