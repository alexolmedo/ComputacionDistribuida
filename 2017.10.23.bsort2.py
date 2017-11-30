import random
import time


def fill(a):
    b=[]
    for i in range (a):
        b.append(random.randint(0,a*2))
    return b

def bsort(c):
	for i in range (len(c),0,-1):
		for j in range (i-1):
			if c[j] > c[j+1]:
				c[j], c[j+1] = c[j+1], c[j]
	return c

def merge(a,b):
    """ Function to merge two arrays """
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


n=10000
start = time.time()

x1=[]
x2=[]

x1=fill(n/2)
x2=fill(n/2)

y1=bsort(x1)
y2=bsort(x2)

y=merge(y1,y2)

end = time.time()
total=end-start

print total