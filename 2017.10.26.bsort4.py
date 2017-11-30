import random
import time
import thread
from threading import Thread


def fillAndSort(list, n):
    for i in range (n):
        list.append(random.randint(0,n*2))
    list=bsort(list)
    return


def bsort(c):
    for i in range (len(c),0,-1):
        for j in range (i-1):
            if c[j] > c[j+1]:
                c[j], c[j+1] = c[j+1], c[j]
    return c


def merge(a,b):
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c


n = 10000
start = time.time()
x1 = []
x2 = []

try:
    t1 = Thread(target = fillAndSort, args=(x1, n/2))
    t2 = Thread(target = fillAndSort, args=(x2, n/2))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    #thread.start_new_thread(fillAndSort, (x1, n/2,))
    #thread.start_new_thread(fillAndSort, (x2, n/2,))
except Exception as errtxt:
    print errtxt

y = merge(x1,x2)

end = time.time()
total=end-start

print total