# Usage: ./nice.sh file_name
#!/bin/bash
# RANDOM=100

# Define a timestamp function
timestamp() {
  date +"%T"
}

while IFS='' read -r line || [[ -n "$line" ]]; do
	echo "$line $(timestamp)"
	taskset 0x3 google-chrome --enable-logging=stderr --v=1 --load-extension=/home/indrajeet/Downloads/Content --new-window "$line" &>/dev/null &
	temp_pid=($(ps -eo pid,comm | awk '$2~/chrome/ {print $1}'))
	for pid in `ps -eo pid,etimes,comm | awk -v h1=${temp_pid[0]} -v h2=${temp_pid[1]} -v h3=${temp_pid[2]} -v h4=${temp_pid[3]} -v h5=${temp_pid[4]} -v h6=${temp_pid[5]} -v h7=${temp_pid[6]} -v h8=${temp_pid[7]} -v h9=${temp_pid[8]} -v h10=${temp_pid[9]} '$1!=h1 && $1!=h2 && $1!=h3 && $1!=h4 && $1!=h5 && $1!=h6 && $1!=h7 && $1!=h8 && $1!=h9 && $1!=h10 && $2>30 && $3~/chrome/ {print $1 $2}'` ; do awk -v to=${to_cfg} `if($2 > to){tasket }; if( kill -15 $pid ; done
	sleep 5
	# sleep $(($RANDOM%20 + 5))
done < "$1"


#the time needs to exponentially increasing increasing and not with constant time intervals like 5 seconds
#he wanted to move everything to python

# Move to python and dont use the for loop and use the taskset to get the PIDS  rather than fetching them everytime
# Allthe results with exponential arrival etime
# https://stackoverflow.com/questions/19152067/execute-linux-command-and-get-pid
# Interrupt and which looks like a callback rather than sleep
# https://stackoverflow.com/questions/27694818/interrupt-sleep-in-bash-with-a-signal-trap
# sprinted -> pid1 pid2 pid3,.... etc and dont sprint it again use PYTHON
# pid1 -> estimated start time note them down 
keep note of power energy and dont exceed budget 
yeah

#you want to check for sprinting and killing in the same command 



