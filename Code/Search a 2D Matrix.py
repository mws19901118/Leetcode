class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        if target<matrix[0][0] or target>matrix[m - 1][n - 1]:      #If target is smaller than the first element or greater than the last element, return false.
            return False
        i = 0
        j = n - 1                                                   #Begin search from the last element in the first row.
        while i < m and j >= 0:
            if matrix[i][j] == target:                              #If find the target, return true.
                return True
            elif matrix[i][j] > target:                             #If current element is smaller than target, target must in the left side of current column.
                j -= 1
            else:                                                   #If current element is greater than target, target must in the lower side of current row.
                i += 1
        return False
