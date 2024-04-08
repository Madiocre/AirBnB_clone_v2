#!/usr/bin/env bash
# Script installs nginx if not installed, creates folders and directories
# and change ownership

apt-get update
apt-get -y install nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' > /data/web_static/releases/test/index.html

ln -s -f /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '/^http {/a\    location /hbnb_static {\n\talias /data/web_static/current;\n\t}' /etc/nginx/sites-enabled/default
service nginx restart
