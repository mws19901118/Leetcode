class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        row=len(matrix)
        if row==0:
            return 0
        column=len(matrix[0])
        if column==0:
            return 0
        maxl=0                                                                    #Record the max side length of squares.
        side=[[0 for i in range(column+1)] for j in range(row+1)]                 #Record current side length of square whose bottom right corner is matrix[i-1][j-1].
        for i in range(1,row+1):
            for j in range(1,column+1):
                if matrix[i-1][j-1]=='1':
                    side[i][j]=min(side[i-1][j],side[i][j-1],side[i-1][j-1])+1    #If matrix[i-1][j-1] is '1', current side length equals 1 plus the min side length of squares whose bottom right corner is matrix[i-2][j-1], matrix[i-1][j-2], matrix[i-2][j-2] respectively.
                    if side[i][j]>maxl:
                        maxl=side[i][j]                                           #Update the max side length.
        return maxl*maxl                                                          #Return the square of maxl.
