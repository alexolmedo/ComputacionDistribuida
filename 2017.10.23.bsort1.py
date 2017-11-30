import random
import time


def fill(a):
    b=[]
    for i in range (a):
        b.append(random.randint(0,a))
    return b

def bsort(c):
	for i in range (len(c),0,-1):
		for j in range (i-1):
			if c[j] > c[j+1]:
				c[j], c[j+1] = c[j+1], c[j]
	return c

n=1000
start = time.time()
x=[]
x=fill(n)
y=bsort(x)

end = time.time()
total=end-start

print total
