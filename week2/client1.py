
import socket 

#Create a socket object

client1 = socket.socket()

client1.connect(('localhost', 9999))

client1.send("hello server1".encode())

response = client1.recv(1024).decode()

print(f'server replied : {response}')

client1.close()



