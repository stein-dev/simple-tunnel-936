#!/bin/sh

folder=../config/

echo Content-type: text/html
echo ""

POST_STRING=`cat`

busybox rm -f ${folder}${POST_STRING}







