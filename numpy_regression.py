import sys

from numpy import *

import matplotlib.pyplot as plt

def powers(lst,lower_pow,upper_pow):
    
    pow_matrix = []
    
    for enetery in lst :
        
        pow_row = [] 
        
        for j in range(lower_pow , upper_pow+1):
            
            pow_row.append(enetery**j)
            
        pow_matrix.append(pow_row)
        
    return array(pow_matrix)


def poly(a,x):
    
    value = 0
    
    for i in range(len(a)):
        
        value += a[i] * (x**i)
    
    return value

def main():

    file_name = sys.argv[1]

    n = int(sys.argv[2])


    data_mtrx = loadtxt(file_name)

    X = data_mtrx[:,0]

    Y = data_mtrx[:,1]

    Xp  = powers(X,0,n)

    Yp  = powers(Y,1,1)


    Xpt = Xp.transpose()

    a = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))

    a = a[:,0]
    
    Y2=[]
    
    for x in X:
        
        Y2.append(poly(a,x))
        
    Y2_smooth = []
        
    X2 = linspace(min(X),max(X),int((max(X)-min(X))/0.2))

    for x2 in X2:
        
        Y2_smooth.append(poly(a,x2))
        
    # plot with the only given data points
    plt.figure("Polynomial regression with out interpolation")

    plt.plot(X,Y,'*')
    
    plt.plot(X,Y2)
    
    plt.title("Polynomial regression with the given data points")
    
    # plot with more data points 
    plt.figure("Linear regression interpolated")

    plt.plot(X,Y,'*')
    
    plt.plot(X2,Y2_smooth)
    
    plt.title("Polynomial regression with more data points")
    
    plt.show()

if __name__ == "__main__":
    
    main()
