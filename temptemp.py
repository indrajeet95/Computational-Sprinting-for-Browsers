import subprocess
import threading

timesnow_actual = []
energy_actual = []
a = 1
def printit():
	if(a == 1):
		return
	threading.Timer(5.0,printit).start()
	cmd = "perf stat -a -r 1 -e power/energy-pkg/ sleep 5"
	p = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out,err = p.communicate()
	timesnow = err.split('\n')[5]
	energy = err.split('\n')[3]
	timesnow_actual.append(float(timesnow.split()[0]))
	energy_actual.append(float(energy.split()[0]))
	print('Total time elapsed : ',sum(timesnow_actual))
	print('Total Joules consumed : ',sum(energy_actual))

printit()

