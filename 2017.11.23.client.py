#!/usr/bin/python

import socket

s = socket.socket()
# host = socket.gethostname()
host = "localhost"
port = 12222

s.connect((host, port))
print 'Conectado a ', host

while True:
    print s.recv(1024)
    z = raw_input("Escribir algo para el servidor: ")
    s.send(z)
    # Halts
    # print '[Esperando respuesta...]'
    