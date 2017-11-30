import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                 # Reserve a port for your service.

s.connect((host, port))
f = open('recibe.txt','wb')
print 'Conectado'
l = s.recv(1024)
conexion = True

while (str(l)!="end"):
    print 'Recibiendo...'
    f.write(l)
    l = s.recv(1024)
    
f.close()
print "Se acabo de recibir"
s.close()