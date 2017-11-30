import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                 # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
f = open('envia.txt','rb')
s.listen(5)                 # Now wait for client connection.
l = f.readline()
c, addr = s.accept()     # Establish connection with client.
print 'Se obtuvo una conexion desde ', addr
while (l):
    print 'Enviando...'
    c.send(l)
    l = f.read(1024)
c.send("end")
f.close()
print "Se acabo de enviar"
c.shutdown(socket.SHUT_WR)
c.close()