import numpy as np

matrix_A = []
matrix_B = []

def getMatrices(a,b):
    global matrix_A ,matrix_B
    matrix_A = a[:]
    matrix_B = b[:]
    return strassenMethod(np.array(matrix_A),np.array(matrix_B))

def spliter(matrix):
    col = matrix.shape[0]//2
    row = matrix.shape[1]//2
    return matrix[:row, :col], matrix[:row, col:], matrix[row:, :col], matrix[row:, col:]

def strassenMethod(x,y):
    if(len(x) == 1):
        return x*y

    A11,A12,A21,A22 = spliter(x)
    B11,B12,B21,B22 = spliter(y)

    M1 = strassenMethod(A11,B12-B22)
    M2 = strassenMethod(A11+A12,B22)
    M3 = strassenMethod(A21+A22,B11)
    M4 = strassenMethod(A22,B21-B11)
    M5 = strassenMethod(A11+A22,B11+B22)
    M6 = strassenMethod(A12-A22,B21+B22)
    M7 = strassenMethod(A11-A21,B11+B12)

    C11 = M5+M4 - M2+M6
    C12 = M1+M2
    C21 = M3+M4
    C22 = M1+M5 - M3-M7

    result = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))
    return result


