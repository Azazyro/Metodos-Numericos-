def suma (A,B):
    if len(A) != len(B):
        print ("No se puede realizar la suma, el número de renglones no es igual")
        return
    if len(A[0]) != len(B[0]):
        print ("No se puede realizar la suma, el número de columnas no es igual")
        return
    C = A
    for i in range(len(A)):
        for j in range (len(A[0])):
            C[i][j] = A[i][j]+B[i][j]
    return C

def resta (A,B):
    if len(A) != len(B):
        print ("No se puede realizar la suma, el número de renglones no es igual")
        return
    if len(A[0]) != len(B[0]):
        print ("No se puede realizar la suma, el número de columnas no es igual")
        return
    C = A
    for i in range(len(A)):
        for j in range (len(A[0])):
            C[i][j] = A[i][j]-B[i][j]
    return C

A = [[1,1],[1,1]]

print(suma(A,A))
print(resta(A,A))
