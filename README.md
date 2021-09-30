# certbot-to-gandi
A script to update my Let's Encrypt certificate using DNS challenge with Gandi's DNS.

It's a bad copy-paste of my `iptogandi` script, done in about 30 minutes, maybe I'll clean it up one day.

## Configuration
The location of the configuration file is currently hard-coded as `/usr/local/etc/certbot-gandi.conf`. The file contains your **private API key**, so it **must not be readable by anyone** except the user running the script.

## Usage
You'll need to setup certbot: https://wiki.archlinux.org/title/Certbot

I added a systemd service and timer to execute `certbot-gandi.py`.
