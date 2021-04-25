class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix) // 2):                                       #According to symmertry, consider n // 2 outer border, n is the dimension of matrix.
            for j in range(len(matrix) - 2 * i - 1):                            #The length of edge of ith outer border is n - 2 * i - 1. The corner point which is joint of 2 edges belongs to the edge in clockwise order.
                temp = matrix[i][i + j]                                         #Let temp be the value of upper edge point.
                matrix[i][i + j] = matrix[-(i + j + 1)][i]                      #Let the value of upper edge be the value of corresponding point in left edge.
                matrix[-(i + j + 1)][i] = matrix[-(i + 1)][-(i + j + 1)]        #Let the value of left edge be the value of corresponding point in lower edge.
                matrix[-(i + 1)][-(i + j + 1)] = matrix[i + j][-(i + 1)]        #Let the value of lower edge be the value of corresponding point in right edge.
                matrix[i + j][-(i + 1)] = temp                                  #Let the value of right edge be the value of corresponding point in upper edge(i.e. temp).
