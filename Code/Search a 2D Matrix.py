class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:                                                             #Check if matrix is empty or matrix row is empty.
            return False                                                                            #If so, return false.
        m, n = len(matrix), len(matrix[0])                                                          #Get the dimensions of matrix.
        start, end, index = 0, m, 0
        while start <= end:                                                                         #Binary search in the first column to find the last row that is not greater than target.
            mid = (start + end) // 2
            if matrix[mid][0] <= target and (mid >= m - 1 or matrix[mid + 1][0] > target):
                index = mid                                                                         #Get the row index of the row which target could belong to.
                break
            elif matrix[mid][0] > target:
                end = mid - 1
            else:
                start = mid + 1
        start, end = 0, n - 1
        while start <= end:                                                                         #Binary search in that row to find target.
            mid = (start + end) // 2
            if matrix[index][mid] == target:
                return True                                                                         #If found, return true.
            elif matrix[index][mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return False                                                                                #Otherwise return false.
