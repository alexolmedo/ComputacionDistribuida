import socket
import threading
import sys

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            print 'Se obtuvo una conexion desde ', address
            client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        size = 1024
        while True:
            try:
                data = client.recv(size)
                if data:
                    # Responder con los mismos datos recibidos
                    respuesta = data

                    logOut = open('log.txt', 'a')
                    logOut.write(data + "\n")

                    client.send(respuesta)
                    #client.shutdown(socket.SHUT_RDWR)
                    #client.close()
                else:
                    raise error('Cliente desconectado')
            except:
                client.close()
                return False

if __name__ == "__main__":
    #Crear un archivo de log vacio
    open('log.txt', 'w').close()

    while True:
        try:
            port_num = int(sys.argv[1])
            break
        except ValueError:
            pass

    ThreadedServer('',port_num).listen()