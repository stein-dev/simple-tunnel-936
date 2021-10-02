#!/bin/sh

S1=`busybox cat /system/etc/autorun.sh | busybox grep /online/simpletunnel/script/startonboot.sh`
S2=`busybox cat /system/etc/autorun.sh | busybox grep /online/simpletunnel/script/cpu_monitor.sh`

if [ -n "$S1" ]; then
    mount -o remount,rw /system /system
    busybox sed -i -e '/\/online\/simpletunnel\/script\/startonboot.sh/d' /system/etc/autorun.sh
fi

if [ -n "$S2" ]; then
    mount -o remount,rw /system /system
    busybox sed -i -e '/\/online\/simpletunnel\/script\/cpu_monitor.sh/d' /system/etc/autorun.sh
fi

rm -rf /online/simpletunnel/
echo "Uninstall completed!"
echo "Rebooting..."
reboot