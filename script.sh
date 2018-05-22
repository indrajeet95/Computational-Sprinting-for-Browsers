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
	for pid in `ps -eo pid,etimes,comm | awk -v h1=${temp_pid[0]} -v h2=${temp_pid[1]} -v h3=${temp_pid[2]} -v h4=${temp_pid[3]} -v h5=${temp_pid[4]} -v h6=${temp_pid[5]} -v h7=${temp_pid[6]} -v h8=${temp_pid[7]} -v h9=${temp_pid[8]} -v h10=${temp_pid[9]} '$1!=h1 && $1!=h2 && $1!=h3 && $1!=h4 && $1!=h5 && $1!=h6 && $1!=h7 && $1!=h8 && $1!=h9 && $1!=h10 && $2>30 && $3~/chrome/ {print $1}'`; do kill -15 $pid ; done
	sleep 5
	# sleep $(($RANDOM%20 + 5))
done < "$1"
