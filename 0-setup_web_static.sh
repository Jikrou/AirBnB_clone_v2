#!/usr/bin/env bash

# a Bash script that sets up your web servers for the deployment of web_static. It must:
#Install Nginx if it not already installed
sudo apt-get update -y
sudo apt-get -y install nginx
#Create the folder /data/ if it doesn’t already exist
#Create the folder /data/web_static/ if it doesn’t already exist
#Create the folder /data/web_static/releases/ if it doesn’t already exist
#Create the folder /data/web_static/shared/ if it doesn’t already exist
mkdir -p /data/web_static/shared/
#Create the folder /data/web_static/releases/test/ if it doesn’t already exist
mkdir -p /data/web_static/releases/test/
#Create a fake HTML file /data/web_static/releases/test/index.html 
#(with simple content, to test your Nginx configuration)
touch /data/web_static/releases/test/index.html
echo " <html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
#Create a symbolic link /data/web_static/current linked to 
#the /data/web_static/releases/test/ folder. If the symbolic link already exists,
#it should be deleted and recreated every time the script is ran.
# Remove the existing symbolic link if it exists
if [ -L /data/web_static/current ]; then
    rm /data/web_static/current
fi
ln -s /data/web_static/releases/test/ /data/web_static/current
#Give ownership of the /data/ folder to the ubuntu user AND group 
#(you can assume this user and group exist). This should be recursive;
#everything inside should be created/owned by this user/group.
chown -R ubuntu:ubuntu /data/
#Update the Nginx configuration to serve the content of 
#/data/web_static/current/ to hbnb_static 
#(ex: https://mydomainname.tech/hbnb_static). Don’t forget to restart
#Nginx after updating the configuration:
#Use alias inside your Nginx configuration

printf '%s\n' "server {
	listen 80;
	server_name onebro.tech;
	add_header X-Served-By 369852-web-01;
	root /data/web_static/releases/test;

	location /hbnb_static/ {
		alias /data/web_static/current/ ;
		index index.html;
	}
	}" > /etc/nginx/sites-available/hbnb_static

sudo ln -sf /etc/nginx/sites-available/hbnb_static /etc/nginx/sites-enabled/
sudo rm -f /etc/nginx/sites-enabled/default

sudo service nginx restart
