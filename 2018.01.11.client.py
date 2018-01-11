import socket
import sys

print sys.argv[0]
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host = raw_input("Nombre de host o IP del servidor? ")
host = sys.argv[1]
port = int(sys.argv[2])
data = sys.argv[3]
print host, port, data

sock.connect((host,port))

sock.send(data)
print "Respuesta: ", sock.recv(1024)