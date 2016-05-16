##4. Write a function that takes a 2D list of integers as input, 
##
##and when it is called increments each item whose sum of the 
##
##two indices is an odd number (i.e. list[0][1], list[3][2]). 
##
##The function does not return anything.



def increment_odd(List: [[int]]) -> None:

     for i in range(len(List)):
         for j in range(len(List[i])):
             # print(L[i][j])
             if (i + j ) %2 != 0 :
                 List[i][j] += 1

##                 
##               for i in range(len(x)):
##
##    for j in range(len(x[i])):
##
##        if (i+j)%2 == 1:
##
##            x[i][j] += 1
##                 

         
L = [[1,2,3], [4,5,6],[7,8,9]]
print(L)

increment_odd(L)
print(L)




