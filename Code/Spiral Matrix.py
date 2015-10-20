class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        result=[]
        m=len(matrix)
        if m==0:
            return result
        n=len(matrix[0])
        if n==0:
            return result
        mine=min(m,n)                                               #Find the min length of edges
        for i in range(mine/2):                                     #Loop for mine/2 times to deal with the outer level.
            for j in range(n-2*i):                                  #Deal with the top line, the ith row, with index starting at i, ending at n-i-1.
                result.append(matrix[i][j+i])
            for j in range(m-2*i-1):                                #Deal with the right line, the (n-1-i)th column, with index starting at i+1, ending at m-i-1.
                result.append(matrix[j+i+1][n-1-i])
            for j in range(n-2*i-1):                                #Deal with the bottom line, the (m-1-i)th row, with index starting at n-2-i, ending at i.
                result.append(matrix[m-1-i][n-2-i-j])
            for j in range(m-2*(i+1)):                              #Deal with the left line, the ith column, with index starting at m-2-i, ending at i+1.
                result.append(matrix[m-2-i-j][i])
        if mine%2==1:                                               #If mine%2 equals 1, there is still a column(m>=n) or a row(m<n) hasn't bee de
            if m>=n:
                for i in range(m-(mine/2)*2):                       #Calculate the number of remaining elements.
                    result.append(matrix[mine/2+i][mine/2])         #Traverse downward starting at matrix[mine/2][mine/2]
            else:
                for i in range(n-(mine/2)*2):                       #Calculate the number of remaining elements.
                    result.append(matrix[mine/2][mine/2+i])         #Traverse rightward starting at matrix[mine/2][mine/2]
        return result
