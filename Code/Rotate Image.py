class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        n=len(matrix)
        for i in range(n/2):                                  #According to symmertry, consider n/2 outer border.
            for j in range(n-2*i-1):                          #The length of edge of ith outer border is n-2*i-1. The corner point which is joint of 2 edges belongs to the edge in clockwise order.
                temp=matrix[i][i+j]                           #Let temp be the value of upper edge point.
                matrix[i][i+j]=matrix[n-1-i-j][i]             #Let the value of upper edge be the value of corresponding point in left edge.
                matrix[n-1-i-j][i]=matrix[n-1-i][n-1-i-j]     #Let the value of left edge be the value of corresponding point in lower edge.
                matrix[n-1-i][n-1-i-j]=matrix[i+j][n-1-i]     #Let the value of lower edge be the value of corresponding point in right edge.
                matrix[i+j][n-1-i]=temp                       #Let the value of right edge be the value of corresponding point in upper edge(i.e. temp).
