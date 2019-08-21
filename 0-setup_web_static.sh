#!/usr/bin/env bash
# check  the server is set up properly

apt-get -y install nginx
ufw allow 'Nginx HTTP'
mkdir -p "/data/"
mkdir -p "/data/web_static/"
mkdir -p "/data/web_static/releases/"
mkdir -p "/data/web_static/shared/"
mkdir -p "/data/web_static/releases/test"
touch "/data/web_static/releases/test/index.html"
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > "/data/web_static/releases/test/index.html"

rm "/data/web_static/current"
ln -sf "/data/web_static/releases/test/" "/data/web_static/current"
chown -R ubuntu:ubuntu "/data/"
sed -i "/listen 80 default_server;/a location /hbnb_static/ {\n alias /data/web_static/current/;\n }\n" /etc/nginx/sites-available/default
service nginx restart
exit 0