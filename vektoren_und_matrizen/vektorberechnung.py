import numpy as np
from numpy import linalg as LA

# Basics
# Creating an array
a = np.array([1, 2, 3, 4])
b = np.zeros(3)
c = np.ones(4)
d = np.empty(5) # 5 random numbers
e = np.arange(6,11,2) # die Zahlen von 6-10 aufwärts in zweier Schritten    [n,(m-1)]
f = np.linspace(6,10,num=4) # in 4 Teilen gleichmässig gespaced             [n, m]
x = np.ones(2, dtype=np.int64) # sets datatype from default:float -> integer
y = np.sort(d) # sorts the random numbers from d going upwards

# Shape & Size of an array
A = np.array([
            [[0, 1, 2, 3],
            [4, 5, 6, 7]],

            [[0, 1, 2, 3],
            [4, 5, 6, 7]],

            [[0 ,1 ,2, 3],
            [4, 5, 6, 7]]
        ])
A1 = A.ndim # gives the amount of dimension / layer of brackets [[[...]]]
A2 = A.size # gives the amount of values inside the array
A3 = A.shape # gives the amount of objects in each layer.

# transposing an array
T = np.transpose(A) # transposes the first and last axes of A
T1 = T.shape

# dot product
Skalarprodukt = np.dot(a,c) # gives the dotproduct a and c

# norm of a vector
Betrag = LA.norm(c) # gives the norm of c


print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(x)
print(y)
print(str(A1)+"\n"+str(A2)+"\n"+str(A3))
print(T)
print(T1)
print(Skalarprodukt)
print(Betrag)