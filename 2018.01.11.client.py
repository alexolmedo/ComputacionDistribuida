import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host = raw_input("Nombre de host o IP del servidor? ")
host = "localhost"
port = input("Puerto del servidor? ")
sock.connect((host,port))
while True:
    data = raw_input("Mensaje: ")
    sock.send(data)
    print "Respuesta: ", sock.recv(1024)