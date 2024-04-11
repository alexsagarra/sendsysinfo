# Send Systeminformation over TEAMS Webhook

<img src="./images/logo.png" width="100" title="logo">

## Setup

Update ;)

```
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip
sudo apt install git
```

clone the Repository

```
git clone https://github.com/alexsagarra/sendsysinfo.git
```

```

cd sendsysinfo
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements_minimal.txt
```

## Script

create the .env file (copy the example)

```
python main.py
```

## CRON

crontab -e
@reboot sleep 10 && /home/zebbra/sendsysinfo/sys_send.sh >> /home/zebbra/sendsysinfo/log.txt 2>&1
@reboot sleep 1 && /home/zebbra/sendsysinfo/sys_send.sh >> /home/zebbra/sendsysinfo/log.txt 2>&1

@reboot /root/backup.sh
sudo systemctl status cron.service
sudo systemctl enable cron.service

## BANNER
https://manytools.org/hacker-tools/ascii-banner/

```
sudo nano /etc/motd
```

```
  #####  #     #  #####     ### #     # ####### #######     #####  ####### #     # ######  
 #     #  #   #  #     #     #  ##    # #       #     #    #     # #       ##    # #     # 
 #         # #   #           #  # #   # #       #     #    #       #       # #   # #     # 
  #####     #     #####      #  #  #  # #####   #     #     #####  #####   #  #  # #     # 
       #    #          #     #  #   # # #       #     #          # #       #   # # #     # 
 #     #    #    #     #     #  #    ## #       #     #    #     # #       #    ## #     # 
  #####     #     #####     ### #     # #       #######     #####  ####### #     # ######  
                                                                                           
                                                                                    
```

## DOCKER

```
curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh
sudo usermod -aG docker ${USER}
groups ${USER}
sudo reboot now
```

```
sudo apt install libffi-dev libssl-dev python3-dev python3 python3-pip
sudo pip install docker-compose
sudo apt install docker-compose
sudo systemctl enable docker
```

```
docker run hello-world
```

```
mkdir wordpress
cd wordpress
nano docker-compose.yml
```

version: '3.6'

services:
wordpress:
image: wordpress:5.7.2
ports: - 80:80
environment: - "WORDPRESS_DB_USER=root" - "WORDPRESS_DB_PASSWORD=vFvpKjJ7HUbkD3wyLDp4"
restart: always
dns: 8.8.8.8
volumes: - /srv/wordpress:/var/www/html

mysql:
image: jsurf/rpi-mariadb
volumes: - /srv/wordpress-mysql:/var/lib/mysql
environment: - "MYSQL_ROOT_PASSWORD=vFvpKjJ7HUbkD3wyLDp4" - "MYSQL_DATABASE=wordpress"
restart: always

phpmyadmin:
image: phpmyadmin:apache
environment: - PMA_ARBITRARY=1
restart: always
ports: - 9999:80
volumes: - /sessions

```
docker-compose up -d
```
