import numpy as np

def lcsAlgo(s1, s2):
    m = len(s1)
    n = len(s2)
    k = np.zeros((m+1,n+1),int)

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                pass
            elif s1[i-1] == s2[j-1]:
                k[i][j] = k[i-1][j-1] + 1
            else:
                k[i][j] = max(k[i-1][j], k[i][j-1])

    index = k[m][n]
    LCS = ["" for x in range(index+1)]
    LCS[index] = ""

    i ,j = m, n
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            LCS[index-1] = s1[i-1]
            i -= 1
            j -= 1
            index -= 1

        elif k[i-1][j] > k[i][j-1]:
            i -= 1
        else:
            j -= 1  
    result = {"LCS":"".join(LCS[:-1]) , "length":len(LCS[:-1])}
    return(result)  




