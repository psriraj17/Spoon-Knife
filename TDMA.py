import math as math

import numpy as np

import matplotlib.pyplot as plt



## Tri Diagonal Matrix Algorithm solver

#A user-defined function which takes four 1D vector.
def TDMAsolver(a, b, c, d):

    n = len(d)  # number of equations
    aa, bb, cc, dd = map(np.array, (a, b, c, d))  # copy the array values
    for i in range(1, n):

        bb[i] = bb[i] - ((aa[i - 1] / bb[i - 1]) * cc[i - 1])
        dd[i] = dd[i] - ((aa[i - 1] / bb[i - 1]) * dd[i - 1])

    xc = bb
    xc[-1] = dd[-1] / bb[-1]

    for il in range(n - 2, -1, -1):
        xc[il] = (dd[il] - cc[il] * xc[il + 1]) / bb[il]


    return xc

# A user-defined function used to generate a 1D array vector based on the prpblem stated.
def generator(n):
    q=[]

#For every updation of "i" value, the value of P is updated and stored in q array.
    for i in range(1,n):
        p= (math.sin(math.radians(2*math.pi*(i/(n-1)))))*50*(1/64)
        q.append(p) # this function inserts the value into array after each iteration.
    q[0]= q[0]+10 #This is the initial boundary condition of adding 10
    q[i-1]= q[i-1]+50 #This is the end boundary condition of adding 50

    return q # returns the array q to d in the call function.


#This function generates required values for the vector a & c.
def gen_a(n):
    z=[]
    for j in range(0,n-1):
        jj= -1.
        z.append(jj)
    return z

#This function genretes the values for vector b.
def gen_b(n):
    z=[]
    for j in range(0,n):
        jj= 2.
        z.append(jj)
    return z
# the function genreates the  mesh elements i.e M= 8,10,16 .... within the range of (0,1).
def x_values(n):
    x=[]
    for k in range(1,n):
        val = k/n
        x.append(val)
    return x

# Generates values of -1 based on the size of the array i.e depending on meshing elements
a = gen_a(8)
# Generates values of 2 based on the size of the array i.e depending on meshing elements
b = gen_b(8)
# Generates values of -1 based on the size of the array  i.e depending on meshing elements
c = gen_a(8)

d = generator(9)
print(d) # print the values of d.


T_x=TDMAsolver(a, b, c, d) #function call
print(T_x)
x= x_values(9) # function call

# Graph ploted against temperature(x) vs x values.
plt.plot(x,T_x)

plt.show()
