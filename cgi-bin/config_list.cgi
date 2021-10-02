#!/bin/sh

echo Content-type: text/html
echo ""

#dir="/mnt/Backup/web-projects/simple-tunnel-936/config"
dir="/online/simpletunnel/config"
configs=`ls $dir`

if [ -n "$configs" ]; then
    echo "$configs"
else
    echo "NULL"
fi