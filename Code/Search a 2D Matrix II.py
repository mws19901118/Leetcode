class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])              #Get the dimensions.
        i, j = 0, n - 1                                 #Starting from the top right corner.
        while i < m and j >= 0:
            if matrix[i][j] == target:                  #If found target, return true.
                return True
            elif matrix[i][j] > target:                 #If current number is greater than target, move left.
                j -= 1
            else:                                       #Otherwise, move down.
                i += 1
        return False                                    #If not found, return false.
