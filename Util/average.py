import os

path = '/Users/indrajeet/Desktop/Comp_Sprint/Results/Organized By Inter-Arrival Time/2.6'
for root,dirs,files in os.walk(path):
	for file in files:
		counter = 0
		sum = 0
		if file.endswith(".csv"):
			f = open(path + '/' + file,'r')
			for line in f:
				if float(line.split(',')[-1]) <= 30000:
					counter += 1
					sum += float(line.split(',')[-1])
			print '\n' + file + '\t'
			print 'Successful Page loads: ' + str(counter)
			print (sum + (100-counter)*30000)/100