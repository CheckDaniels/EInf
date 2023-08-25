a = [1,2,3]
b = [4,5,6]
Skalarprodukt = 0
for x in a: Skalarprodukt += x*b[x-1]
print(Skalarprodukt)