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
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" >> "/data/web_static/releases/test/index.html"
fi
rm "/data/web_static/current"
ln -s "/data/web_static/releases/test/" "/data/web_static/current"
chown -R ubuntu:ubuntu "/data/"
sed "/listen 80 default_server;/a \nlocation /hbnb_static {\n alias /data/web_static/current/\n }\n" /etc/nginx/sites-enabled/default
service nginx restart
exit 0
