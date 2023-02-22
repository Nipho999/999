from pytube import YouTube
from pytube.cli import on_progress
import os
import sys
import time
import colorama
from colorama import Fore
from slowprint.slowprint import *
os.system('clear')
slowprint(Fore.BLUE + f"╔═╗╔═╗──╔═══╗\n║║╚╝║║──║╔═╗║\n║╔╗╔╗╠══╬╝╔╝║\n║║║║║║╔╗╠╗╚╗║\n║║║║║║╚╝║╚═╝║\n╚╝╚╝╚╣╔═╩═══╝\n─────║║\n─────╚╝\n╔═══╗──────────╔╗────────╔╗\n╚╗╔╗║──────────║║────────║║\n─║║║╠══╦╗╔╗╔╦═╗║║╔══╦══╦═╝╠══╦═╗\n─║║║║╔╗║╚╝╚╝║╔╗╣║║╔╗║╔╗║╔╗║║═╣╔╝\n╔╝╚╝║╚╝╠╗╔╗╔╣║║║╚╣╚╝║╔╗║╚╝║║═╣║\n╚═══╩══╝╚╝╚╝╚╝╚╩═╩══╩╝╚╩══╩══╩╝",0.4)
urlVid = input(Fore.RED + "\n Paste your youtube link below: \n ")
myVid = YouTube(urlVid,on_progress_callback=on_progress)
slowprint(Fore.BLUE + "\n###### 🇵​ 🇱​ 🇪​ 🇦​ 🇸​ 🇪​ 🇼​ 🇦​ 🇮​ 🇹​.....####",0.5)
slowprint(Fore.RED + "\n ....loading....",0.2)
slowprint(Fore.WHITE + f"\n >>Channel : {myVid.author}",0.4)
slowprint(Fore.YELLOW + f"\n >>Tittle : {myVid.title}",0.4)
slowprint(Fore.RED + f"\n >>Played    : {myVid.views}",0.4)
video = myVid.streams.filter(only_audio=True).first()
previousprogress = 0
def on_progress(stream, chunk, bytes_remaining):
    global previousprogress
    total_size = yt.stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    liveprogress = (int)(bytes_downloaded / total_size * 100)
    if liveprogress > previousprogress:
        previousprogress = liveprogress
        print(liveprogress)
destination = ('/storage/emulated/0/download/')
out_file = video.download(output_path=destination)
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)
slowprint(Fore.BLUE + myVid.title + "\n 𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍ed 𝚌𝚘𝚖𝚙𝚕𝚎𝚝𝚎",0.4)
