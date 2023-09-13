a = [4,5,6]
b = [7,9,4]
def Skalarprodukt(u,v):
    Sp = 0
    for x,y in zip(u,v):
        Sp += x*y
    return Sp
print(Skalarprodukt(a,b))