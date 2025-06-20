import socket     #import module 


s = socket.socket()         #create socket object
print(' Socket Created')

s.bind(('localhost', 9999))

s.listen(3)
print('Waiting for connection...')


while True:
 c , addrs = s.accept()

 name = c.recv(1024).decode()  #receive data from client
 print('Connected to:', addrs , name)
 c.send(b'Welcome to the server!')  #send bytes