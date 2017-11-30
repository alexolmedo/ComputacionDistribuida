import socket               # Import socket module
import sqlite3

# Conexion a base sqlite
conn = sqlite3.connect('log.db')
sqlite = conn.cursor()

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                 # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
f = open('envia.txt','r')
s.listen(5)                 # Now wait for client connection.
l = f.readline()
c, addr = s.accept()     # Establish connection with client.
print 'Se obtuvo una conexion desde ', addr
numLinea=1
while (l):
    print 'Enviando...'
    c.send(l)
    linea="INSERT INTO conexion VALUES ('envia.txt','localhost','"+str(numLinea)+"','10h00')"
    print linea
    sqlite.execute(linea)
    numLinea+=1
    l = f.readline()
c.send("EOF")
f.close()
print "Se acabo de enviar"
c.shutdown(socket.SHUT_RDWR)
c.close()

conn.commit()
conn.close()