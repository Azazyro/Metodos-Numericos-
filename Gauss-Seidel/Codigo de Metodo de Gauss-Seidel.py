def getx1(x2,x3):
    return 

def getx2(x1,x3):
    return 

def getx3(x1,x2):
    return 

x1 = 0
x2 = 0
x3 = 0
E = 0.01

for i in range(100):
    x1i = getx1(x2,x3)
    x2i = getx2(x1i,x3)
    x3i = getx3(x1i,x2i)
    
    Ex1 = abs(x1-x1i)
    Ex2 = abs(x2-x2i)
    Ex3 = abs(x3-x3i)
    
    x1 = x1i
    x2 = x2i
    x3 = x3i
    
    if Ex1 < E and Ex2 < E and Ex3 < E:
        break

print(x1,x2,x3)
