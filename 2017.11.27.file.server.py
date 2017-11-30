import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                 # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
f = open('envia.txt','r')
log = open('logSend.txt','a')
s.listen(5)                 # Now wait for client connection.
l = f.readline()
c, addr = s.accept()     # Establish connection with client.
print 'Se obtuvo una conexion desde ', addr
numLinea=1
while (l):
    print 'Enviando...'
    c.send(l)
    log.write(str(numLinea)+"\n")
    numLinea+=1
    l = f.readline()
c.send("EOF")
f.close()
log.close()
print "Se acabo de enviar"
c.shutdown(socket.SHUT_WR)
c.close()