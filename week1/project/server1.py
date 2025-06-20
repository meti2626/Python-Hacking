import socket 

server1 = socket.socket()

server1.bind(('localhost', 9999))

server1.listen(1)

print("Server is listening...")


##accept the connection

conn , addr = server1.accept()

#recieve data from client

data = conn.recv(1024).decode()


print(f"Received data from {addr}: {data}")


#send a reply bck to the client 

conn.send("Hello from server1!  Message received.".encode())

conn.close()