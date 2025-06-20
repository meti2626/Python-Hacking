import socket

c = socket.socket()  # create socket object

c.connect(('localhost', 9999))  # connect to the server


name = input("enter your name: ")
c.send(bytes(name, 'utf-8'))  # send name as bytes

print(c.recv(1024).decode())