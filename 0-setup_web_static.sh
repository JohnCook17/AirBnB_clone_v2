#!/usr/bin/env bash
# check if the server is set up properly

if ! which nginx
then
apt get nginx
fi
if ! -d "/data/" 
then 
mkdir "/data/"
fi
if ! -d "/data/web_static/"
then
mkdir "/data/web_static/"
fi
if ! -d "/data/web_static/releases/"
then
mkdir "/data/web_static/releases/"
fi
if ! -d "/data/web_static/shared/"
then
mkdir "/data/web_static/shared/"
fi
if ! -d "/data/web_static/releases/test/"
then
mkdir "/data/web_static/releases/test"
fi
if ! -f "/data/web_static/releases/test/index.html"
then
touch "/data/web_static/releases/test/index.html"
echo "this is a test" >> "/data/web_static/releases/test/index.html"
fi
rm "/data/web_static/current"
ln -s "/data/web_static/current" "/data/web_static/releases/test/"
chown -R ubuntu:ubuntu "/data/"
sed "/server {/a location /hbnb_static {\n alias /data/web_static/current/\n }\n" /etc/nginx/nginx.conf
service nginx restart
exit 0
