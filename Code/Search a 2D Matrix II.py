class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        row=len(matrix)
        if row==0:
            return False
        column=len(matrix[0])
        if column==0:
            return False
        if target<matrix[0][0] or target>matrix[row-1][column-1]:
            return False
        if row>1:                               #If there are more than 1 rows, split them into 2 parts, search the target in the 2 parts respectively then return the or operation of the results.
            return self.searchMatrix(matrix[:row/2], target) or self.searchMatrix(matrix[row/2:], target)
        else:                                   #If there is only 1 row, binary search the target in that row.
            start=0
            end=column-1
            while start<=end:
                mid=(start+end)/2
                if matrix[row-1][mid]==target:
                    return True
                elif matrix[row-1][mid]>target:
                    end=mid-1
                else:
                    start=mid+1
            return False
