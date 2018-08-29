def nextnumber(g, o, inp):
    matrix= [[0 for i in range(g+o)] for k in range(g+2)]
    for i in range(g):
        matrix[0][i]=inp[i]

    for k in range(1,g+2):
        for p in range(0,g-k):
            matrix[k][p]=matrix[k-1][p+1]-matrix[k-1][p]
        if matrix[k].count(matrix[k][0])==len(matrix[k])-(o+k):
            continue
    
    for n in reversed(range(0, k)):
        for j in range(1, g+o):
            matrix[n][j]=matrix[n][j-1]+matrix[n+1][j-1]
    
    finalstr=''
    for l in range(g, g+o):
        finalstr+= str(matrix[0][l])+' '
    print finalstr

tcases=int(raw_input())
for _ in xrange(tcases):
    g, o= map(int, raw_input().split(' '))
    inp= map(int, raw_input().split(' '))
    nextnumber(g, o, inp)
