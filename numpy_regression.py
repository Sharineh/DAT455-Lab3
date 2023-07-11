import sys

from numpy import *

import matplotlib.pyplot as plt

def powers(lst,lower_pow,upper_pow):
    
    np_power_lst = zeros((len(lst),(upper_pow-lower_pow+1)))
    
    for i in range(np_power_lst.shape[0]):
        
        for j in range(lower_pow , upper_pow+1):
            
            np_power_lst[i,j-lower_pow] = lst[i] ** (j-lower_pow)
            
    return np_power_lst


def poly(a,x):
    
    value1 = []
    
    for i in range(len(a)):
        
        value1.append(a[i] * (x**i))
    
    value1 = sum(value1)
    
    return value1



""" file_name = sys.argv[1]

n = int(sys.argv[2])
 """
 
n = 2

file_name = "chirps-modified.txt"

data_mtrx = loadtxt(file_name)

X = []

Y = []

for point in data_mtrx:
    
    X.append(point[0])
    
    Y.append(point[1])

Xp  = powers(X,0,n)

Yp  = powers(Y,1,1)

Xpt = Xp.transpose()

a = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))

a = a[:,0]

Y2 = []

for x in X:
    
    value = poly(a,x)
    
    Y2.append(value)
    
    

# Different plots of the data and the regression model
plt.figure()

plt.plot(X,Y,'ro')

plt.figure()

plt.plot(X,Y2)

plt.show()


