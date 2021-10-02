#!/bin/bash

set -x

adb connect 192.168.8.1:5555
sleep 2
adb push simpletunnel.zip /tmp/
adb shell mkdir -p /online/simpletunnel || true
adb shell busybox unzip /tmp/simpletunnel.zip -d /online/simpletunnel
adb shell busybox chmod 755 /online/simpletunnel/script/*.*
adb shell sh /online/simpletunnel/script/install.sh