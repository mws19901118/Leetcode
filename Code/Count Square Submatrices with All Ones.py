class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])                                                                                  #Get matrix dimensions.
        result = 0                                                                                                          #Count squares.
        sideLength = [[0 for j in range(n)] for i in range(m)]                                                              #Use a matrix with same dimension to store the max square side length of each coordinate.
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i > 0 and j > 0:                                                                                     #If current coordinate is not left side or top side, its max square side length is the min square side length of left coordinate, top coordiante, left top coordinate plus one.
                        sideLength[i][j] = min(sideLength[i - 1][j], sideLength[i][j - 1], sideLength[i - 1][j - 1]) + 1
                    else:                                                                                                   #Otherwise, it's just one.
                        sideLength[i][j] = 1
                    result += sideLength[i][j]                                                                              #The number of squares whose bottom right corner is current coordinate equals the max square side length.
        return result
