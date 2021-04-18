def lcsub(string1, string2):
    m=len(string1)
    n=len(string2)

    L=[ [0]*(n+1) for i in range(m+1) ]

    maxlen = 0
    maxlen_cor = ()
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                L[i][j] = 0
            elif string1[i-1] == string2[j-1]:
                L[i][j] = 1 + L[i-1][j-1]
                if L[i][j] > maxlen:
                    maxlen = L[i][j]
                    maxlen_cor = (i,j)

    csub = ''
    ptr = maxlen_cor[0]-1
    while maxlen > 0:
        csub = string1[ptr] + csub  
        ptr-=1
        maxlen -= 1
    return csub

def lcs(string1, string2):
    m=len(string1)
    n=len(string2)

    L=[ [None]*(n+1) for i in range(m+1) ]

    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                L[i][j] = 0
            elif string1[i-1] == string2[j-1]:
                L[i][j] = 1 + L[i-1][j-1]
            else:
                L[i][j] = max( L[i-1][j] , L[i][j-1])
    return L[m][n]


if __name__ == "__main__":
    string1='ABCDBCB'
    string2='BCBABCD'
    m=lcsub(string1,string2)
