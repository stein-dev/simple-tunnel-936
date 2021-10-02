#!/bin/sh

echo Content-type: text/html
echo ""

PREV_TOTAL=0
PREV_IDLE=0

while true; do
    CPU=`busybox sed -n 's/^cpu\s//p' /proc/stat`
    IDLE=`busybox sed -n 's/^cpu\s//p' /proc/stat | busybox awk '{ print $4}'`

    if [ -n "$CPU" ]; then
        TOTAL=0
        for VAL in $CPU; do
            #echo $val
            TOTAL=$(( TOTAL + VAL ))
        done

        DIFF_IDLE=$((IDLE-PREV_IDLE))
        DIFF_TOTAL=$((TOTAL-PREV_TOTAL))
        DIFF_USAGE=$((( 1000*(DIFF_TOTAL-DIFF_IDLE)/DIFF_TOTAL+5)/10 ))

        echo "$DIFF_USAGE%"
        PREV_TOTAL="$TOTAL"
        PREV_IDLE="$IDLE"
        sleep 1
    else
        echo "NULL"
        exit 1
    fi
	
done    