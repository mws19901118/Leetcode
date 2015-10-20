class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        matrix=[[0 for i in range(n)] for j in range(n)]
        count=1                                         #Record the current number to be added to the matrix.
        for i in range(n/2):
            for j in range(n-2*i):                      #Deal with the top line, the ith row, with index starting at i, ending at n-i-1.
                matrix[i][j+i]=count
                count+=1
            for j in range(n-2*i-1):                    #Deal with the right line, the (n-1-i)th column, with index starting at i+1, ending at n-i-1.
                matrix[j+i+1][n-1-i]=count
                count+=1
            for j in range(n-2*i-1):                    #Deal with the bottom line, the (n-1-i)th row, with index starting at n-2-i, ending at i.
                matrix[n-1-i][n-2-i-j]=count
                count+=1
            for j in range(n-2*(i+1)):                  #Deal with the left line, the ith column, with index starting at n-2-i, ending at i+1.
                matrix[n-2-i-j][i]=count
                count+=1
        if n%2==1:                                      #If n%2==1, add the point in the center of the matrix.
                matrix[n/2][n/2]=count
        return matrix
