""" Send System-Information over Request URL """

import platform
import requests
import os
import socket
import pymsteams
from uuid import getnode as get_mac
from pprint import pprint as pp
from dotenv import load_dotenv
import time

load_dotenv()
WEBHOOK = os.getenv("WEBHOOK", "value does not exist")

requests.packages.urllib3.disable_warnings()


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


def send_webhook2(jsondata: dict):
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


def try_to_send_get_request(mehtod, url, payload=None):
    """try to send a request"""
    sleeptime: int = 10
    maxtry: int = 20
    counter: int = 0
    error: str = ""
    response = ""

    while counter != maxtry:

        if counter == maxtry:
            maxtry = maxtry * 2
        try:
            print(f"Counter = {counter}")
            response = requests.request(
                mehtod, url=url, data=payload, timeout=10, verify=False
            )
            if response.status_code == 200:
                print("get request 200")
                break

        except requests.exceptions.HTTPError as errh:
            error = f"Count {counter} HTTP Error {errh.args[0]}"
            counter = counter + 1
            time.sleep(sleeptime)
        except requests.exceptions.ReadTimeout as errrt:
            error = f"Count {counter} Time out {errrt}"
            counter = counter + 1
            time.sleep(sleeptime)
        except requests.exceptions.ConnectionError as conerr:
            error = f"Count {counter} Connection error {conerr}"
            counter = counter + 1
            time.sleep(sleeptime)
        except requests.RequestException as e:
            error = f"Count {counter} RequestException {e}"
            counter = counter + 1
            time.sleep(sleeptime)
        except KeyboardInterrupt:
            error = f"Count {counter} Someone closed the program {e}"
            counter = counter + 1
            time.sleep(sleeptime)
        except:
            error = f"Count {counter} except xy"
            counter = counter + 1
            time.sleep(sleeptime)
        print(error)
        # finally:
        #     print("The 'try except' is finished")
    return response


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
    response = try_to_send_get_request("GET", "https://api.ipify.org")
    # url = "https://api.ipify.org"
    # response = requests.get(url)
    ip_address = response.text
    return ip_address


def main():
    """workflow"""
    sysinfodata = sysinfo()
    # pp(sysinfodata)
    send_webhook(sysinfodata)


if __name__ == "__main__":
    main()
