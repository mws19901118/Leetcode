class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])                                                                                  #Get the dimensions.
        result = 0                                                                                                          #Count squares.
        sideLength = [[0 for j in range(n + 1)] for i in range(m + 1)]                                                      #Use a matrix with same dimension to store the max square side length of each coordinate.
        for i, j in product(range(m), range(n)):                                                                            #Traverse matrix.
            if matrix[i][j]:                                                                                                #If current coordinate is 1, its max square side length is the min square side length of left coordinate, top coordiante, left top coordinate plus one.                                                                             #If current coordinate is not left side or top side, 
                sideLength[i][j] = min(sideLength[i - 1][j], sideLength[i][j - 1], sideLength[i - 1][j - 1]) + 1
                result += sideLength[i][j]                                                                                  #The number of squares whose bottom right corner is current coordinate equals the max square side length.
        return result
