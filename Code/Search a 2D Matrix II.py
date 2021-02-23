class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])              #Get the dimensions.
        i, j = 0, n - 1                                 #Starting from the top right corner.
        while i < m and j >= 0:                         #While valid, maintain the top right corner of possible area where target is in.
            if matrix[i][j] == target:                  #If found target, return true.
                return True
            elif matrix[i][j] > target:                 #If current number is greater than target, all numbers in same column are greater than target, so move left.
                j -= 1
            else:                                       #Otherwise, all numbers in same row are smaller than target, move down.
                i += 1
        return False                                    #If not found, return false.
