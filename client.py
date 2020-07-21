import socket
sock = socket.socket()

sock.connect(('localhost', 12456))
data = sock.send('привет, я твой клиент'.encode())

sock.close

print(data)
