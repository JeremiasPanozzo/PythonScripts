#!/bin/bash

function ctrl_c(){
        echo -e "\n\n[!] Saliendo...\n"
        tput cnorm; exit 1
}

trap ctrl_c INT

tput civis

max_parallel=50  
seq 1 65535 | xargs -n 1 -P $max_parallel -I {} bash -c 'timeout 1 bash -c "echo '' > /dev/tcp/10.10.0.130/{}" 2>/dev/null && echo "[+] PORT {} - ACTIVE"' 

tput cnorm
