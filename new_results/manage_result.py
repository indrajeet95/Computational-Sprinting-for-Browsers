import os
from os import listdir
from os.path import isfile, join

import re
import csv
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt

import pandas as pd
import seaborn as sns

#####METHOD TO AVERAGE DATA from CSV#####
def average_time(csv_filepath, index):
	total = 0
	lines = 0
	with open(csv_filepath, "rb") as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		reader.next()
		for row in reader:
			#print row[8]
			total += float(row[index]) #7 - processing time; #8 - total run time
			lines += 1
	avg = total/lines
	return str(avg)

mypath = os.getcwd()
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath,f))]

print len(onlyfiles)

#CHANGES TO BE MADE#
#service_dict according to your set of experiments#
#timeout_dict, budget_dict & arrival_rate_dict as well#

job_dict = ["jacobi", "spkmeans", "spstream", "bfs", "nn", "kmeans"] #JOB NAME
arrival_rate_dict = ["0.1", "0.2", "0.5", "0.8", "0.9"] #ARRIVAL RATE
budget_dict = ["1600", "3200", "6400", "12800"] #BUDGET
timeout_dict = ["50", "100", "150", "200"] #TIMEOUT
service_dict = {"jacobi":0.0107,"spkmeans":0.0074,"spstream":0.0833,"bfs":0.0208,"nn":0.0588,"kmeans":0.0147,"empty":0.0833} #SERVICE

print "Enter the indices to fix the parameters for a job"
job = input("Enter 1st job index "  + str(job_dict) + " | 999 for ALL: ")
arrival_rate = input("Enter 1st arrival rate index " + str(arrival_rate_dict) + " | 999 for ALL: ")
budget = input("Enter 1st budget index " + str(budget_dict) + " | 999 for ALL: ")
timeout = input("Enter 1st timeout index " + str(timeout_dict) + " | 999 for ALL: ")
arange = input("Enter 1st experiment range (1,2,3...9) | 999 for ALL: ")

jobA = "[a-z]*" if (job == 999) else str(job_dict[job])
arrival_rateA = "[0-9]*" if (arrival_rate == 999) else str(arrival_rate_dict[arrival_rate])
budgetA = "[0-9]*" if (budget == 999)  else str(budget_dict[budget])
timeoutA = "[0-9]*" if (timeout == 999)  else str(timeout_dict[timeout])
serviceA = "00[0-9]*" if (job == 999) else str(service_dict[jobA])
actual_arrival_rateA = "00[0-9]*" if (job == 999 or arrival_rate == 999) else str(float(service_dict[jobA])*float(arrival_rateA))
exp_rangeA = "[0-9]*" if (arange == 999) else str(arange) + "[0-9]*"

numexp = "30"
cache_config = ".*"
job_mix = "[a-z]+-[a-z]+-[a-z]+-[a-z]+-[a-z]+-[a-z]+"
counter = 0

regexA = jobA + "_\." + actual_arrival_rateA[2:] + "_" + timeoutA + "_0\." + serviceA[2:] + "_" + numexp + "_" + cache_config + "_" + budgetA + "_" + job_mix + "_" + exp_rangeA + "_" + "[0-9].csv"

#my_regex = r"[a-z]+_.[0-9]+_[0-9]+_0.[0-9]+_[0-9]+_.*_[0-9]+_[a-z]+-[a-z]+-[a-z]+-[a-z]+-[a-z]+-[a-z]+_[0-9]+_[0-9].csv"

first_filter = []
job_ids = []
for file in onlyfiles:
	if(re.search(regexA, file)):
		first_filter.append(file)
		job_ids.append(file.split('_')[-2])
		counter = counter + 1

for a in first_filter:
	print a

#for job_id in job_ids:
#	print job_id

print "Total results found: " + str(counter)

job = input("\nEnter 2nd job index "  + str(job_dict) + " | 999 for ALL: ")

jobB = "[a-z]*" if (job == 999) else str(job_dict[job])

counterb = 0
regexBholder = []
regexB = jobB + "_\." + "[0-9]*" + "_" + "[0-9]*" + "_0\." + "[0-9]*" + "_" + "[0-9]*" + "_" + ".*" + "_" + "[0-9]*" + "_" + job_mix + "_"

for job_id in job_ids:
	regexBholder.append(regexB + job_id + "_" + "[0-9].csv")

second_filter = []
for file in onlyfiles:
	for regexBval in regexBholder:
        	if(re.search(regexBval, file)):
                	second_filter.append(file)
			counterb = counterb + 1

for b in second_filter:
	print b

print "Total results found: " + str(counterb)

###########GENERATING PLOTS###############

arrival_rates = []
timeouts = []
budgets = []
avg_qtimes = []
avg_proctimes = []
avg_runtimes = []

for file_name in second_filter:
	arrival_rate_on_file = float(file_name.split('_')[1])
        org_arrival_rate = float(service_dict[jobB])*arrival_rate_on_file
        arrival_rates.append(org_arrival_rate)
	timeouts.append(file_name.split('_')[2])	
	budgets.append(file_name.split('_')[8])
	avg_qtimes.append(average_time(file_name,6))
	avg_proctimes.append(average_time(file_name,7))
	avg_runtimes.append(average_time(file_name,8))

#print arrival_rates
#print timeouts
#print budgets
#print avg_qtimes
#print avg_proctimes
#print avg_runtimes

columns = ['arrival_rate','timeout','budget','avg_qtime','avg_proctime','avg_runtime']
df = pd.DataFrame(columns=columns)
c = 0
for i,j,k,l,m,n in zip(arrival_rates,timeouts,budgets,avg_qtimes,avg_proctimes,avg_runtimes):
	df.loc[c] = [i,j,k,l,m,n]
	c += 1

df['arrival_rate']=df['arrival_rate'].astype(float)
df['timeout']=df['timeout'].astype(int)
df['budget']=df['budget'].astype(int)
df['avg_qtime']=df['avg_qtime'].astype(float)
df['avg_proctime']=df['avg_proctime'].astype(float)
df['avg_runtime']=df['avg_runtime'].astype(float)

#print df

df_final = df[['arrival_rate','timeout','budget','avg_qtime','avg_proctime','avg_runtime']].groupby(['arrival_rate','timeout','budget']).mean()
df_final.reset_index(inplace=True)
print df_final

sns.set(style="whitegrid")
ax = sns.barplot(x="timeout", y="avg_runtime", hue="budget", data=df_final)
title = jobB + " vs " + jobA
#ax.text(0.85, 0.85,'Text Here', fontsize=9)
ax.set_title(title)
fig=ax.get_figure()
fig.savefig("output.png")
