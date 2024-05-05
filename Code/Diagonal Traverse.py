class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])                                                                                #Get dimensions.
        result = []
        for i in range(m + n - 1):                                                                                  #For a matrix with dimension m and n, there are m + n - 1 diagonals.
            (u, v) = (-1, 1) if not i & 1 else (1, -1)                                                              #Calculate the delta based on direction.
            (x, y) = (min(i, m - 1), max(0, i - m + 1)) if not i & 1 else (max(0, i - n + 1), min(i, n - 1))        #Calculate the starting position based on direction.
            while 0 <= x < m and 0 <= y < n:                                                                        #Move forward until reaches the end.
                result.append(mat[x][y])                                                                            #Append current number to result.
                x += u
                y += v
        return result
