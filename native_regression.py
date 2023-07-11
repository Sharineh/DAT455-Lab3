import sys

from matrix import *

import matplotlib.pyplot as plt

file_name = sys.argv[1]
#file_name = "chirps.txt"

data_mtrx = loadtxt(file_name)

X = []

Y = []

for point in data_mtrx:
    
    X.append(point[0])
    
    Y.append(point[1])

Xp = powers(X,0,1)

Yp = powers(Y,1,1)

Xpt = transpose(Xp)

[[b],[m]] = matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp))

m_times_x = [m * element for element in X]

predictd_num_of_chirps = [b + element for element in m_times_x]

# Different plots of the data and the regression model

plt.figure()

plt.plot(X,Y,'*')

plt.plot(X,predictd_num_of_chirps)

plt.title("Model and actual data")


plt.figure()

plt.plot(X,Y,'o')

plt.title("Actual data")



plt.figure()

plt.plot(X,predictd_num_of_chirps)

plt.title("Linear regression model")

plt.show()


