def createMatriz(m,n,v):
    C = []
    for i in range(m):
        C.append([])
        for j in range(n):
            C[i].append(v)
    return C

def getDimensiones(A):
    return (len(A),len(A[0]))

def sumMatrices(A,B):
    Am,An = getDimensiones(A)
    Bm,Bn = getDimensiones(B)
    if Am != Bm or An != Bn:
        print("Las dimensiones son diferentes")
        return []
    C = createMatriz(Am,An,0)
    for i in range(Am):
        for j in range(An):
            C[i][j] = A[i][j] + B[i][j]
    return C

def restaMatrices(A,B):
    Am,An = getDimensiones(A)
    Bm,Bn = getDimensiones(B)
    if Am != Bm or An != Bn:
        print("Las dimensiones son diferentes")
        return []
    C = createMatriz(Am,An,0)
    for i in range(Am):
        for j in range(An):
            C[i][j] = A[i][j] - B[i][j]
    return C

def mulMatrices(A,B):
    Am,An = getDimensiones(A)
    Bm,Bn = getDimensiones(B)
    if An != Bm:
        print("Las matrices no son conformables")
        return []
    C = createMatriz(Am,Bn,0)
    for i in range(Am):
        for j in range(Bn):
            for k in range(An):
                C[i][j] += A[i][k] * B[k][j]
    return C
def getMenorMatriz(A,r,c):
    m,n = getDimensiones(A)
    C = createMatriz(m-1,n-1,0)
    for i in range(m):
        if i == r:
            continue
        for j in range(n):
            if j == c:
                continue
            Ci = i
            if i > r:
                Ci = i - 1
            Cj = j
            if j > c:
                Cj = j -1
            C[Ci][Cj] = A[i][j]
    return C

def detMatriz(A):
    m,n = getDimensiones(A)
    if m != n:
        print("La matriz no es cuadrada")
        return -1
    if m == 1:
        return m
    if m == 2:
        return  A[0][0]*A[1][1] - A[0][1]*A[1][0]
    det = 0
    for j in range(n):
        det += (-1)**(j)*A[0][j]*detMatriz(getMenorMatriz(A,0,j))
    return det

def getMatrizAdyacente(A):
    m,n = getDimensiones(A)
    C = createMatriz(m,n,0)
    for i in range(m):
        for j in range(n):
            C[i][j] = (-1)**(i+j)*detMatriz(getMenorMatriz(A,i,j))
    return C

def getMatrizTranspuesta(A):
    m,n = getDimensiones(A)
    C = createMatriz(n,m,0)
    for i in range(m):
        for j in range(n):
            C[j][i] = A[i][j]
    return C

def getMatrizInversa(A):
    detA = detMatriz(A)
    if detA == 0:
        print("La matriz no tiene inversa")
        return 0
    At =  getMatrizTranspuesta(A)
    adyAt =  getMatrizAdyacente(At)
    m,n = getDimensiones(A)
    C = createMatriz(m,n,0)
    for i in range(m):
        for j in range(n):
            C[i][j] = (1/detA)*adyAt[i][j]
    return C

####
# Sistema a resolver
# 4*x1 - x2 + x3 - x1*x4
# -x1 + 3*x2 - 2*x3 - x2*x4
# x1 - 2*x2 + 3*x3 - x3*x4
# 2*x1 + 2*x2 + 2*x3 - 1

####
# Esta parte se debe cambiar y corresponde
# Al sistema a resolver
def n(x1,x2,x3,x4):
    return 4*x1 - x2 + x3 - x1*x4

def dnd1(x1,x2,x3,x4):
    return 4-x4

def dnd2(x1,x2,x3,x4):
    return -1

def dnd3(x1,x2,x3,x4):
    return 1

def dnd4(x1,x2,x3,x4):
    return -x1

def m(x1,x2,x3,x4):
    return -x1 + 3*x2 - 2*x3 - x2*x4

def dmd1(x1,x2,x3,x4):
    return -1

def dmd2(x1,x2,x3,x4):
    return 3-x4

def dmd3(x1,x2,x3,x4):
    return -2

def dmd4(x1,x2,x3,x4):
    return -x2

def o(x1,x2,x3,x4):
    return x1 - 2*x2 + 3*x3 - x3*x4

def dod1(x1,x2,x3,x4):
    return 1

def dod2(x1,x2,x3,x4):
    return -2

def dod3(x1,x2,x3,x4):
    return 3-x4

def dod4(x1,x2,x3,x4):
    return -x3

def p(x1,x2,x3,x4):
    return 2*x1 + 2*x2 + 2*x3 - 1

def dpd1(x1,x2,x3,x4):
    return 2

def dpd2(x1,x2,x3,x4):
    return 2

def dpd3(x1,x2,x3,x4):
    return 2

def dpd4(x1,x2,x3,x4):
    return 0

###
#Esta es la matriz Jacobiana
# Corresponde a las derivadas parciales
A = [[dnd1, dnd2, dnd3, dnd4],[dmd1, dmd2, dmd3, dmd4], [dod1, dod2, dod3, dod4], [dpd1, dpd2, dpd3, dpd4]]
###
# Esta es una matriz con las funciones originales
D = [[n],[m], [o], [p]]

####
#Valores iniciales
C = [[1],[1],[1],[1]]
####
# Error deseado
itera=0

for i in range(100):
    itera = itera + 1
    Am,An = getDimensiones(A)
    ## Calcular D en el punto C
    Di =createMatriz(Am,1,0)
    for k in range(Am):
        for j in range(1):
            Di[k][j] = D[k][j](C[0][0],C[1][0],C[2][0],C[3][0])
    Ai = createMatriz(Am,An,0)
    for k in range(Am):
        for j in range(An):
            Ai[k][j] = A[k][j](C[0][0],C[1][0],C[2][0],C[3][0])
    invAi = getMatrizInversa(Ai)
    Bi = restaMatrices(C,mulMatrices(invAi,Di))
    Ce = restaMatrices(C,Bi)
    print ("Error en iteración ",itera," = ",Ce)
    if itera==4:
        C = Bi
        break
    C = Bi

print("Los valores son",C)
