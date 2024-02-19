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

## BANNER

```
sudo nano /etc/motd
```

```d88P 888~~  888~~\  888~~\  888~-_        e            888~-_   888
  d88P  888___ 888   | 888   | 888   \      d8b           888   \  888
 d88P   888    888 _/  888 _/  888    |    /Y88b          888    | 888
d88P    888    888  \  888  \  888   /    /  Y88b         888   /  888
d88P     888    888   | 888   | 888_-~    /____Y88b        888_-~   888
d88P____ 888___ 888__/  888__/  888 ~-_  /      Y88b       888      888

```
