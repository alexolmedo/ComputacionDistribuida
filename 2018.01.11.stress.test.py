import os

for i in range(10000):
    stringTerminal = "python 2018.01.11.client.py '127.0.0.1' 12222 'Holatest" + str(i) + "'"
    os.system(stringTerminal) 
 