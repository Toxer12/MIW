import numpy as np

data =np.loadtxt('Dane.txt', dtype=int)

#print(data)
#print(data[4])
#print(data[0][4])

def row_one():
    for x in data:
        print(" ")
        for y in x:
            print(y)

row_one()
