import socket
import sys

# El cliente se ejecuta con cliente.py [IP] [Puerto] [Mensaje] 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = sys.argv[1]
port = int(sys.argv[2])
data = sys.argv[3]

sock.connect((host,port))

sock.send(data)
print "Respuesta: ", sock.recv(1024)