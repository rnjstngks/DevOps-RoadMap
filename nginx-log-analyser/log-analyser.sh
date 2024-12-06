#!/bin/bash

# 분석할 로그 파일
LOG_FILE="nginx-access.log"

# 1. Top 5 IP addresses with the most requests
echo "Top 5 IP addresses with the most requests:"
awk '{print $1}' "$LOG_FILE" | sort | uniq -c | sort -nr | head -5 | awk '{printf "%6s requests - %s\n", $1, $2}'
echo

# 2. Top 5 most requested paths
echo "Top 5 most requested paths:"
awk -F\" '{print $2}' "$LOG_FILE" | awk '{print $2}' | sort | uniq -c | sort -nr | head -5 | awk '{printf "%6s requests - %s\n", $1, $2}'
echo

# 3. Top 5 response status codes
echo "Top 5 response status codes:"
awk '{print $9}' "$LOG_FILE" | sort | uniq -c | sort -nr | head -5 | awk '{printf "%6s requests - %s\n", $1, $2}'
echo

# 4. Top 5 user agents
echo "Top 5 user agents:"
awk -F\" '{print $6}' "$LOG_FILE" | sort | uniq -c | sort -nr | head -5 | awk '{printf "%6s requests - %s\n", $1, $2}'
echo
