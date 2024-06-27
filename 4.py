import os
import time
import colorama
from colorama import Fore
from slowprint.slowprint import *
os.system('clear')


slowprint(Fore.BLUE + "------------SUBDOMAINS FINDER MAIN HELP------------", 0.2)
print("***************************************************\n")
slowprint(Fore.RED + " REQUIREMENTS \n ", 0.3)
slowprint(Fore.YELLOW + "      1. Termux-Api APK \n      2. Common sense \n      3. Internet Connection\n      4. python", 0.1)
print("***************************************************")

x = " \nNOTE !!! \n\n To Scan Subdomains run \n \n:>python 1.py -d example.com -o hosts.txt\n \nreplace example.com with you host/domain..\n \n hosts.txt file will be saved on the current directory \n  after scanning subdomains \n \n -o is for output ... \n you can save the output file to your prefered directory \n \n Example \n python 1.py -d example.com -o /storage/emulated/0/Download/hosts.txt \n \nthis will save the hosts.txt on your downloads directory\n \n"
y = " To find Working SNI/BUG HOST  \n \n choose option 1 from the menu \n"
z = " To Download on youtube choose option 3 from menu \n\n"
d = " TO Reverse IP or Domain choose option 2 from menu \n"
slowprint(Fore.RED + x, 0.2)
slowprint(Fore.GREEN + y + z + d, 0.2)
print(Fore.BLUE + "***************************************************")
slowprint(Fore.RED + "this is for educational purposes only ..\n im not responsible\n for any illegal usage perfomed by user", 0.4)
print("****************************************************\n")
for i in range(25, 0, -1):
    print(Fore.BLUE + f"reading time left: {i} seconds")
    time.sleep(1)
os.system('clear')
