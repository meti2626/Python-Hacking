import socket 

server1 = socket.socket()

server1.bind(('localhost', 12345))

server1.listen(1)

print("Server is listening...")