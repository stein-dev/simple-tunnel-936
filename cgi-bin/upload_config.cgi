#!/bin/sh

folder=../config/

CR=`busybox printf '\r'`
HOME="http://192.168.8.1:9090/"
#HOME="http://127.0.0.1:8090/"

echo Content-type: text/html
echo ""

echo '<!doctype html>'
echo '<html lang="en">'
echo '<head>'
echo '<meta charset="utf-8">'
echo '<meta name="viewport" content="width=device-width, initial-scale=1">'
echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'

echo '<link href="../css/bootstrap.min.css" rel="stylesheet">'
echo '<link href="../css/mycss.css" rel="stylesheet">'
echo '<link href="../css/dark-mode.css" rel="stylesheet">'

echo '<title>Simple Tunnel 936</title>'
echo '</head>'
echo '<body>'

echo '<script>'
echo 'setTimeout(function(){'
echo 'window.location.href = "'$HOME'";'
echo '}, 5000);'
echo '</script>'
      
echo '<div class="container">'
echo '<header class="mb-auto">'
echo '      <h3 class="text-center">Simple Tunnel</h3>'
echo '      <p class="text-muted text-center">▀▄▀▄▀▄ @pigscanfly ▄▀▄▀▄▀</p>'
echo '      <nav class="nav justify-content-center float-right">'
echo '        <a class="nav-link active" href="#">Home</a>'
echo '        <a class="nav-link active" href="#">IP Hunter</a>'
echo '        <a class="nav-link active" href="#">Options</a>'
echo '        <a class="nav-link active" href="#">Help</a>'
echo '        <a class="nav-link active" href="#">About</a>'
echo '        <div class="nav-link">'
echo '          <div class="form-check form-switch">'
echo '            <input class="form-check-input" type="checkbox" id="darkSwitch">'
echo '            <label class="form-check-label" for="darkSwitch">Dark Mode</label>'
echo '          </div>'
echo '          <script src="../js/dark-mode-switch.min.js"></script>'
echo '        </div>'
echo '      </nav>'
echo '    </header>'
# echo '<div class="row">'
# echo '<div class="col-sm-12">'
# echo '<h4 class="card-title text-center">SIMPLE TUNNEL 936</h4>'
# echo '<h6 class="small text-muted text-center">▀▄▀▄▀▄ @pigscanfly ▄▀▄▀▄▀</h6>'
# echo '<div class="col-sm-12">'
echo '<div class="text-center"><img id="loader" src="../assets/loading.gif"></div>'
# echo '</div>'

# echo '</div>'
# echo '</div>'
# echo '</div>'

if [ "$CONTENT_LENGTH" = "197" ] || [ "$CONTENT_LENGTH" = "0" ]; then
    echo '<h6 class="small text-danger text-center">No OpenVPN config selected. Redirecting to homepage in 5 seconds...</h6>'
    exit 1
fi


while read -r line; do
  #get file name of uploaded file
  echo "$line" | busybox grep "filename" > /dev/null && file=`echo "$line"|busybox cut -d\" -f4`
  test x"$line" = x"" && break
  test x"$line" = x"$CR" && break
  
done

filename=`busybox basename "$file"`
ext="${filename##*.}"
filex=`busybox basename $filename .ovpn`
ncount=`busybox echo -n $filex | busybox wc -m`

if [ "$ncount" -gt "8" ]; then
    echo '<h6 class="small text-danger text-center">File Name: ' $filename
    echo '</h6>'
    echo '<h6 class="small text-danger text-center">File name must not be longer than 8 characters. Redirecting to homepage in 5 seconds...</h6>'
    exit 1
fi

if [ "$ext" != "ovpn" ]; then
    echo '<h6 class="small text-danger text-center">File Name: ' $filename
    echo '</h6>'
    echo '<h6 class="small text-danger text-center">Invalid OpenVPN config. Redirecting to homepage in 5 seconds...</h6>'
    exit 1
fi

if []

#Uploading config
echo '<h6 class="small text-success text-center">File Name: ' $filename
echo '</h6>'
echo '<h6 class="small text-success text-center">OpenVPN config uploaded successfully. Redirecting to homepage in 5 seconds...</h6>'
busybox cat >"${folder}${filename}"
busybox sed -i '$ d' ${folder}${filename}

echo '</body>'
echo '</html>'

