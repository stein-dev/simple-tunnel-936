#!/bin/sh

echo Content-type: text/html
echo ""

# memfree=`busybox awk '/MemFree/{print $(NF-1)}' /proc/meminfo`
# memtotal=`busybox awk '/MemTotal/{print $(NF-1)}' /proc/meminfo`

mem_used=`busybox free -m | busybox grep ^Mem | busybox tr -s ' ' | busybox cut -d ' ' -f 3`
mem_total=`busybox free -m | busybox grep ^Mem | busybox tr -s ' ' | busybox cut -d ' ' -f 2`

if [ -n "$mem_used" ]; then
    echo "$mem_used MB / $mem_total MB"
else
    echo "NULL"
fi