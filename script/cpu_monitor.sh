#!/bin/sh

PREV_TOTAL=0
PREV_IDLE=0

mount -o remount,rw /system

while true; do
	CPU=`busybox sed -n 's/^cpu\s//p' /proc/stat`

	IDLE=`busybox sed -n 's/^cpu\s//p' /proc/stat | busybox awk '{ print $4}'`

	TOTAL=0

	for VAL in $CPU; do
	    TOTAL=$(( TOTAL + VAL ))
	done

	DIFF_IDLE=$((IDLE-PREV_IDLE))
	DIFF_TOTAL=$((TOTAL-PREV_TOTAL))
	DIFF_USAGE=$(((1000*(DIFF_TOTAL-DIFF_IDLE)/DIFF_TOTAL+5)/10 ))

	echo "$DIFF_USAGE%" > /online/simpletunnel/script/cpu.info
	PREV_TOTAL="$TOTAL"
	PREV_IDLE="$IDLE"

	#busybox timeout 1s busybox tail -f /dev/null
	sleep 1
done
