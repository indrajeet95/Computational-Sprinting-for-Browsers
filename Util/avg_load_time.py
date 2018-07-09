import os
import sys

temp = sys.argv[1]
path = '/Users/indrajeet/Desktop/Comp_Sprint/Results/' + temp
for root,dirs,files in os.walk(path):
	for file in files:
		counter = 0
		sum = 0
		times = []
		if file.endswith(".csv"):
			f = open(path + '/' + file,'r')
			for line in f:
				if int(line.split(',')[-1]) <= 30000:
					times.append(int(line.split(',')[-1]))
					counter = counter + 1
					sum += float(line.split(',')[-1])
			for no in range(0,100-counter):
				times.append(int(30000))
			times.sort()
			median = float(times[49])/1000
			average = (sum + (100-counter)*30000)/100000
			percentile_75 = float(times[74])/1000
			percentile_85 = float(times[84])/1000
			percentile_95 = float(times[94])/1000
			print '\n' + file
			#print 'No of Successful Page Loads: ' + str(counter)
			#print 'Avg. Load time: ' + str(average) #divide by 100 for no of entries and 1000 for getting in seconds
			#print 'Median Load Time: ' + str(median)
			print '75th Percentile: ' + str(percentile_75)
			#print '85th Percentile: ' + str(percentile_85)
			#print '95th Percentile: ' + str(percentile_95)


#Constructing tables is what we are looking for here
#there are two types of tables: energy budget as a major constant and timeout for sprinting as a major constant

#EB vs EC 
#EB vs ALT
#EB vs PL
#EB vs MLT
#EB vs 75TH
#TFS vs EC
#TFS vs ALT