import random
import time
import threading


def fill(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append( [0] * columnas)

    for i in range(filas):
        for j in range(columnas):
            matriz[i][j] = random.randint(0, 100)
    return matriz


def multiplicacion(A, B, matRes, hilo):
    for i in range(hilo*len(A)/8, (hilo+1)*len(A)/8):
        for j in range(len(B[0])):
            for k in range(len(B)):
                matRes[i][j] += A[i][k]*B[k][j]
    return matRes


def matrixmult (A, B):
    C = [[0 for col in range(len(B[0]))] for row in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k]*B[k][j]
    return C

a = fill(64,64)
b = fill(64,64)
c = [[0 for columnas in range(64)] for filas in range(64)]

print a
print b

def startjoin_all(thread_array):
    for t in thread_array:
        t.start()

    for t in thread_array:
        t.join()

threads = []
start = time.time()

for hilo in range(8):
    threads.append(threading.Thread(target=multiplicacion, args=(a, b, c, hilo)))
startjoin_all(threads)

end = time.time()

print (end-start)



inicio = time.time()
res = matrixmult(a,b)
fin = time.time()
print (fin-inicio)




