# core/ui.py
import sys, time, os
from colorama import init
from termcolor import colored

def show_loader():
    load_str = "preparing the time machine portal for voyager...."
    animation = "|/-\\"
    counttime = 0
    i = 0
    while counttime != 100:
        time.sleep(0.075)
        load_str_list = list(load_str)
        x = ord(load_str_list[i])
        y = x - 32 if x > 90 else x + 32
        if x != 32 and x != 46:
            load_str_list[i] = chr(y)
        res = ''.join(load_str_list)
        sys.stdout.write("\r" + res + animation[counttime % 4])
        sys.stdout.flush()
        load_str = res
        counttime += 1
        i = (i + 1) % len(load_str)
   # os.system("cls" if os.name == "nt" else "clear")
    print()

def print_banner():
    init()
    print("""
████████╗██╗░░██╗███████╗  ████████╗██╗███╗░░░███╗███████╗
╚══██╔══╝██║░░██║██╔════╝  ╚══██╔══╝██║████╗░████║██╔════╝
░░░██║░░░███████║█████╗░░  ░░░██║░░░██║██╔████╔██║█████╗░░
░░░██║░░░██╔══██║██╔══╝░░  ░░░██║░░░██║██║╚██╔╝██║██╔══╝░░
░░░██║░░░██║░░██║███████╗  ░░░██║░░░██║██║░╚═╝░██║███████╗
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ░░░╚═╝░░░╚═╝╚═╝░░░░░╚═╝╚══════╝

███╗░░░███╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗███████╗
████╗░████║██╔══██╗██╔══██╗██║░░██║██║████╗░██║██╔════╝
██╔████╔██║███████║██║░░╚═╝███████║██║██╔██╗██║█████╗░░
██║╚██╔╝██║██╔══██║██║░░██╗██╔══██║██║██║╚████║██╔══╝░░
██║░╚═╝░██║██║░░██║╚█████╔╝██║░░██║██║██║░╚███║███████╗
╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝ v3.0""")
    print(colored('         An OSINT Framework for Way Back Machine\n', 'green'))
    print(colored('Coded with Love by Anmol K Sachan (@Fr13ND0x7f) & Arjun Chaudhary (Chaudhary_S4h4b)\n','green')) 
