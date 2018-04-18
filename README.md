# Computational-Sprinting-for-Browsers
Implement sprinting techniques on Chrome based on network activity observed in the local system

hartools

A small command line application for converting HAR (HTTP Archive) files to CSV (comma seperated values).
./har2csv --in <source> --out <destination>
  
 ./har2csv --help
 
 If an error stating that heap space is not enough in Java occurs, use a system with higher RAM capacity.
 
script.sh : This script is used for running experiments by loading Google Chrome with the extension that has been designed to store the network activity for each web page loaded. The list of web pages to be loaded can be provided in a seperate file such as "Top 50 Pages". We use taskset to launch Google-Chrome on certain cores to eventually measure the power consumption.
