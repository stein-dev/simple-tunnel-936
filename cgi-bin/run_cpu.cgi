#!/bin/sh

echo Content-type: text/html
echo ""

busybox start-stop-daemon -S -x /online/simpletunnel/script/cpu_monitor.sh -b