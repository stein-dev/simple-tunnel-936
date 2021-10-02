#!/bin/sh

echo Content-type: text/html
echo ""

WANIP=`busybox ip -4 -o addr show wan0 | busybox awk '{print $6}'`

if [ -n "$WANIP" ]; then
    echo "$WANIP"
else
    echo "127.0.0.1"
fi