""" Send System-Information over Request URL """

import platform
import requests
import os
import socket
import pymsteams
from uuid import getnode as get_mac
from pprint import pprint as pp
from dotenv import load_dotenv

load_dotenv()
WEBHOOK = os.getenv("WEBHOOK", "value does not exist")


def send_webhook(jsondata: dict):
    """send MS TEAMS Webhook"""
    message = "Systeminformation: "
    for raw in jsondata:
        # print(f"{raw}: {jsondata[raw]}")
        message += f"- {raw}: {jsondata[raw]} \n "

    myTeamsMessage = pymsteams.connectorcard(WEBHOOK)
    myTeamsMessage.color("#F8C471")
    myTeamsMessage.text(message)
    myTeamsMessage.send()
    print("webhook send")
    print("message: ", message)
    return True


def sysinfo():
    """collect all system data"""
    sysinfodata = {}
    sysinfodata["hostname"] = platform.node()
    sysinfodata["net-mac"] = get_mac()
    sysinfodata["net-ip"] = socket.gethostbyname(platform.node())
    sysinfodata["net-public_ip"] = get_public_ip_address()
    # sysinfodata["machine"] = platform.machine()
    sysinfodata["version"] = platform.version()
    sysinfodata["platform"] = platform.platform()
    # sysinfodata["uname"] = platform.uname()
    sysinfodata["system"] = platform.system()
    # sysinfodata["processor"] = platform.processor()
    return sysinfodata


def get_public_ip_address():
    """check connection and lookup for public ip"""
    url = "https://api.ipify.org"
    response = requests.get(url)
    ip_address = response.text
    return ip_address


def main():
    """workflow"""
    sysinfodata = sysinfo()
    pp(sysinfodata)
    send_webhook(sysinfodata)


if __name__ == "__main__":
    main()
