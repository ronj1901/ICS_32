  # set the diagonal element to 0


L = [[1,2,3],[4,5,6],[7,8,9],[10,11,12,13,14]]

for i in range(len(L)):
    for j in range(len(L)):

        if   i < len(L[i]):
            
            L[i][i] = 0
            L[-i-1][0] = 0
    


print(L)




