#!/usr/bin/env bash
# Install and setup Nginx web server
sudo apt-get update -qq

# Install Nginx
sudo apt-get install nginx -y

# Create these directories if they don't already exists
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Create the index.html file
sudo touch /data/web_static/releases/test/index.html

# Insert dummy HTML into the index.html file
sudo echo "<html>
  <head>
  </head>
  <body>
    <h1>Dummy content</h2>
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link ../current linked to ../releases/test/ folder.
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

# Give recuesive ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

# Serve the content of /data/web_static/current/ to hbnb_static using alias configuration
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# Restart Nginx
sudo service nginx restart
