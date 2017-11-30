import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                 # Reserve a port for your service.

s.connect((host, port))
f = open('recibe.txt','wb')
log = open('logRecv.txt','a')
print 'Conectado'
l = s.recv(1024)
numLineas=1
while (True):
    if str(l) == "EOF":
        break
    print 'Recibiendo...'
    f.write(l)
    log.write(str(numLineas)+"\n")
    numLineas+=1
    l = s.recv(1024)
    
f.close()
print "Se acabo de recibir"
s.close()