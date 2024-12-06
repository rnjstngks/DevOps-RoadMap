#!/bin/bash

echo "Total CPU Usage"
top -bn1|grep "Cpu(s)"

echo "\nTotal memory usage (Free vs Used including percentage)"
free -m | awk 'NR==2{printf "Usage: %.2f%%, Free: %.2f%%\n", $3*100/$2, $4*100/$2}'

echo "\nTotal disk usage (Free vs Used including percentage)"
df -h | grep '^/dev/sda5' | awk '{used+=$3; avail+=$4; total+=$2} END {printf "Usage: %.2f%%, Free: %.2f%%\n", used*100/(used+avail), avail*100/(used+avail)}'

echo "\nTop 5 process by CPU usage"
ps -eo pid,comm,%cpu --sort=-%cpu|head -n 6

echo "\nTop 5 process by memory usage"
ps -eo pid,comm,%mem --sort=-%mem|head -n 6