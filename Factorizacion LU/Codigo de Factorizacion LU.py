def createMatriz(m,n,v):
    C = []
    for i in range (m):
        C.append([])
        for j in range (n):
            C[i].append(v)
    return C

U = createMatriz(3,3,0)
U[0] = [1,1,1]
U[1] = [1,-1,0]
U[2] = [-1,0,1]


L = createMatriz(3,3,0)
L[0] = [1,0,0]
L[1] = [0,1,0]
L[2] = [0,0,1]

C = createMatriz(3,1,0)
C[0] = [20]
C[1] = [5]
C[2] = [4]

for i in range(3):
    if U[i][i] == 0:
        print("La matriz no tiene LU")
        break
    for j in range(i+1,3):
        c = -1*U[j][i] / U[i][i]
        L[j][i] = -1*c
        for k in range(3):
            U[j][k] += c*U[i][k]
            
print("Matriz U:",U)
print("Matriz L:",L)
print(" ")

Z = createMatriz(3,1,0)
for i in range (3):
    Z[i][0] = C[i][0]
    for j in range(3):
        if i == j:
            break
        Z[i][0] -= L[i][j]*Z[j][0]
print("Matriz Z:",Z)
print(" ")

B = createMatriz(3,1,0)
for i in range (2,-1,-1):
    B[i][0] = Z[i][0]
    for j in range(2,-1,-1):
        if i == j:
            break
        B[i][0] -= U[i][j]*B[j][0]
    B[i][0] = B[i][0]/U[i][i]
print("Matriz Solución:",B)
