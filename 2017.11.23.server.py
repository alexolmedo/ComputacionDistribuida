#!/usr/bin/python

import socket

s = socket.socket()
# host = socket.gethostname()
host = "localhost"
port = 12222
s.bind((host, port))

s.listen(5)
c = None

while True:
   if c is None:
       # Halts
       print '[Esperando la conexion...]'
       c, addr = s.accept()
       print 'Se obtuvo una conexion desde ', addr
   else:
       # Halts
       print '[Esperando respuesta...]'
       print c.recv(1024)
       q = raw_input("Escribir algo para el cliente: ")
       c.send(q)