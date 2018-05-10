import subprocess

def subprocess_cmd(command):
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    return proc_stdout


a = subprocess_cmd("ps -eo pid,comm | awk '$2~/chrome/ {print $1}'")
print a
#output1 = subprocess.Popen(['ps','-eo','pid,comm','|','awk','"$2~/chrome/ {print $1}"'],stdout=subprocess.PIPE).communicate()[0]
#print output1
#output = subprocess.Popen(['ps','-eo','pid,etimes,comm','|','awk','-v','','','',''],stdout=subprocess.PIPE).communicate()[0]
#print output

#ps -eo pid,etimes,comm | awk -v h1=${temp_pid[0]} -v h2=${temp_pid[1]} -v h3=${temp_pid[2]} -v h4=${temp_pid[3]} -v h5=${temp_pid[4]} -v h6=${temp_pid[5]} -v h7=${temp_pid[6]} -v h8=${temp_pid[7]} -v h9=${temp_pid[8]} -v h10=${temp_pid[9]} '$1!=h1 && $1!=h2 && $1!=h3 && $1!=h4 && $1!=h5 && $1!=h6 && $1!=h7 && $1!=h8 && $1!=h9 && $1!=h10 && $2>30 && $3~/chrome/ {print $1 $2}'
