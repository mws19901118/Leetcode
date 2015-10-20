class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        row=len(matrix)
        if row==0:
            return False
        column=len(matrix[0])
        if column==0:
            return False
        start=0
        end=row-1
        while start+1<=end:                                         #Binary search for the row where target belongs to(The statement start+1<=end is to prevent index out of bound).
            mid=(start+end)/2
            if matrix[mid][0]<=target and matrix[mid+1][0]>target:
                start=mid                                           #Find the row.
                break
            elif matrix[mid][0]>target:
                end=mid
            else:
                start=mid+1
        rowIndex=start
        start=0
        end=column-1
        while start<=end:                                           #Binary search for the target in the row it should belong to.
            mid=(start+end)/2
            if matrix[rowIndex][mid]==target:
                return True                                         #If find target, return true.
            elif matrix[rowIndex][mid]>target:
                end=mid-1
            else:
                start=mid+1
        return False                                                #If can not find target, return false.
