import socket
sock = socket.socket()
a = str(input('Enter target server: '))
d = int(input('Enter target server port: '))
sock.connect((a, d))
b = str(input('Enter target fucking ip: '))
data = sock.send(b.encode())

sock.close

print(data)
