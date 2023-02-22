import subprocess
import os
import sys
import time
import colorama
from colorama import Fore
from slowprint.slowprint import *
os.system('clear')
slowprint(Fore.BLUE +"\n [+] script   : >> youtube-Downloader\n [+] Author   : >> Nipho999 \n [+] Github   : >> Nipho999\n [+] ----------MENU-------\n",0.7)
slowprint(Fore.WHITE +"\n******************************************\n",0.3)

while True:
    slowprint(Fore.BLUE + "Please choose an option:",0.5)
    print(Fore.YELLOW +"1. VIDEOS/MP4")
    print(Fore.YELLOW + "2. AUDIO/MP3")
    print(Fore.RED + "3. EXIT")

    choice = input("> ")

    if choice == "1":
        subprocess.run(["python", "videos.py"])
    elif choice == "2":
        subprocess.run(["python", "music.py"])
    elif choice == "3":
        break
    else:
        print("Invalid option. Please restart.")
