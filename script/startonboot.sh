#!/bin/sh

mkdir -p /dev/net
busybox /dev/net/tun c 10 200
busybox httpd -p 9090 -h /online/simpletunnel/
busybox sh /online/simpletunnel/script/cpu_monitor.sh