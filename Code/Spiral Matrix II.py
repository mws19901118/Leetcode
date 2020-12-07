class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for i in range(n)] for j in range(n)]              #Initialize the matrix.
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]                 #Initialize directions in spiral order.
        length, x, y, number = n - 1, 0, 0, 1                           #Initial spiral length is n - 1; initial position is (0, 0); initial number is 1.
        while length > 0:                                               #Traverse while spiral length is greater than 0.
            for dx, dy in directions:                                   #Traverse each direction in spiral order.
                for i in range(length):                                 #Fill the matrix for each spiral arm.
                    matrix[x + i * dx][y + i * dy] = number + i
                x += length * dx                                        #Update x position.
                y += length * dy                                        #Update y position.
                number += length                                        #Update number.
            x, y, length = x + 1, y + 1, length - 2                     #Increase x and y by 1 and decrease length by 2 to enter next inner spiral matrix.
        if length == 0:                                                 #If length is 0, there is one last number to fill in the center of matrix. If cannot be filled in traverse.
            matrix[x][y] = number
        return matrix                                                   #Return matrix.
