#!/bin/sh

S1=`busybox cat /system/etc/autorun.sh | busybox grep /online/simpletunnel/script/startonboot.sh`
#2=`busybox cat /system/etc/autorun.sh | busybox grep /online/simpletunnel/script/cpu_monitor.sh`

if [ -n "$S1" ]; then
	sleep 0
else
	mount -o remount,rw /system /system
	echo /online/simpletunnel/script/startonboot.sh >> /system/etc/autorun.sh
fi

# if [ -n "$S2" ]; then
# 	sleep 0
# else
# 	mount -o remount,rw /system /system
# 	echo busybox sh /online/simpletunnel/script/cpu_monitor.sh >> /system/etc/autorun.sh
# fi

echo Install completed!
sleep 1
echo Rebooting modem. Please wait...
atc AT^RESET