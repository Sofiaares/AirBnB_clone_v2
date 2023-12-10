#!/bin/bash

# Install Nginx if not installed
if ! [ -x "$(command -v nginx)" ]; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/{releases/test,shared}

# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create the desired symbolic link structure
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Set ownership for the directories
sudo chown -R ubuntu:ubuntu /data/web_static

# Update Nginx configuration
config="server {
    listen 80 default_server;
    listen [::]:80 default_server;
    server_name _;
    location /hbnb_static {
        alias /data/web_static/current/;
    }
    error_page 404 /404.html;
    location = /404.html {
        root /usr/share/nginx/html;
        internal;
    }
}"

# Add updated configuration to Nginx
sudo bash -c "echo '$config' > /etc/nginx/sites-available/default"

# Restart Nginx
sudo systemctl restart nginx

exit 0
