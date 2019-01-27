class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        length = len(grid)
        width = len(grid[0])
        result = 0
        for i in range(length - 2):                           #Traverse each square in the matrix.
            for j in range(width - 2):
                columnSum = [0, 0, 0]
                rowSum = [0, 0, 0]
                diagonalSum = [0, 0]
                integers = [0] * 15
                for k in range(3):
                    for l in range(3):
                        rowSum[k] += grid[i + k][j + l]       #Calculate row sums.
                        columnSum[k] += grid[i + l][j + k]    #Calculate column sums.
                        integers[grid[i + k][j + l]] += 1     #Check the integerss are between 1 to 9.
                    diagonalSum[0] += grid[i + k][j + k]      #Calculate diagonal sums.
                    diagonalSum[1] += grid[i + 2 - k][j + k]
                if all(map(lambda x: x == 15, rowSum)) and all(map(lambda x: x == 15, columnSum)) and all(map(lambda x: x == 15, diagonalSum)) and all(map(lambda x: x == 1, integers[1:10])):
                    result += 1
        return result
