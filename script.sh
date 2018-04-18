# Usage: ./nice.sh file_name
#!/bin/bash
# RANDOM=100
while IFS='' read -r line || [[ -n "$line" ]]; do
	taskset 0x1 google-chrome --enable-logging=stderr --v=1 --load-extension=/home/indrajeet/Downloads/Content --new-window "$line" &>/dev/null &
	temp_pid=($(ps -eo pid,etime,comm | awk '$3~/chrome/ {print $1}'))
	for pid in `ps -eo pid,etime,comm | awk -v h1=${temp_pid[0]} -v h2=${temp_pid[1]} -v h3=${temp_pid[2]} -v h4=${temp_pid[3]} -v h5=${temp_pid[4]} '$1!=h1 && $1!=h2 && $1!=h3 && $1!=h4 && $1!=h5 && $2~/^00:30/ && $3~/chrome/ {print $1}'` ; do kill -15 $pid ; done
	sleep 10
	# sleep $(($RANDOM%20 + 5))
done < "$1"
