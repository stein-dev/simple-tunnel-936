#!/bin/sh

echo Content-type: text/html
echo ""

folder=../config/

POST_STRING=`cat`

# if [ -n "$POST_STRING" ]; then
#     touch "${folder}${POST_STRING}no1"
#     exit 1   
# fi   

filename=`echo "$POST_STRING" | busybox sed 's/<br>/\n/g' | busybox tail -n1`


# if [[ "${filename}" =~ "^[a-zA-Z0-9.-]+$" ]]; then
#     touch "${folder}${filename}-no"

# else
#     touch "${folder}${filename}-yes"
# fi

tmp=`echo $filename | busybox sed 's/.ovpn//'`

# if [[ $tmp =~ ^[[:alnum:]]+$ ]];then
#       touch "${folder}${filename}-yes-${tmp}"
# else
#       touch "${folder}${filename}-no-${tmp}"
# fi

if ! [[ "$tmp" =~ [^a-zA-Z0-9\ ] ]]; then
  touch "${folder}${filename}-yes-${tmp}"
else
  touch "${folder}${filename}-no-${tmp}"
fi

# echo $POST_STRING > "${folder}test001.ovpn"

# echo $POST_STRING | busybox sed 's/<br>/\n/g' | busybox sed '$d' > "${folder}${filename}"








