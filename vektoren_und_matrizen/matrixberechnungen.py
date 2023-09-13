import numpy as np
# Matrix-Vector-multiplication
A = np.array([[1,2,3,4,5,6],
             [3,7,4,8,2,9],
             [9,9,5,6,3,8],
             [1,0,0,4,3,1]])

a = np.array([4,5,8,3,6,5]) #multiplies the Matrix A with the vector a: A*a = x

x = np.dot(A,a)

# Dotproduct
b = np.array([1,2,3])
c = np.array([4,5,6])
Skalarprodukt = np.dot(b,c)

# Transposing
AT = np.transpose(A)

# Matrix-multiplication
T = np.array([[2,1],
              [6,4]])       # ist die inverse Matrix von U: T = U^-1
U = np.array([[2 ,-0.5],
              [-3,1   ]])   # ist die inverse Matrix von T: U = T^-1
TU = (T@U) # gibt die Einheitsmatrix E wieder: E = ([[1,0],[0,1]])

print(x)
print(Skalarprodukt)
print(str(AT)+"\n")
print(TU)
