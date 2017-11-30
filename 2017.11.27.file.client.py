import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                 # Reserve a port for your service.

s.connect((host, port))
f = open('recibe.txt','wb')
print 'Conectado'
l = s.recv(1024)

while (True):
    print 'Recibiendo...'
    f.write(l)
    l = s.recv(1024)
    if str(l) == "EOF":
        break
    
f.close()
print "Se acabo de recibir"
s.close()