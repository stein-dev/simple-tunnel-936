#!/bin/sh

folder=../config/

CR=`busybox printf '\r'`
# HOME="http://192.168.8.1:8080/"
HOME="http://127.0.0.1:8090/"

echo Content-type: text/html
echo ""

POST_STRING=`cat`

echo $POST_STRING > ../config/test002.txt

while read -r line; do
  #get file name of uploaded file
  echo "$line" | grep "filename" > /dev/null && file=`echo "$line"|busybox cut -d\" -f4`
  test x"$line" = x"" && break
  test x"$line" = x"$CR" && break
  
done

filename=`busybox basename "$file"`
ext="${filename##*.}"

cat > "${folder}${file}"
busybox sed -i '$ d' ${folder}${file}

