class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:                           #Check the dimensions are not empty.
            return []
        m, n = len(matrix), len(matrix[0])                        #Get dimensions.
        x, y = 0, 0                                               #Initialize start point.
        result = []                                               #Initialize result.
        for i in range(m + n - 1):                                #For a matrix with dimension m and n, there are m + n - 1 diagonals.
            while True:                                           #Traverse current diagonal.
                result.append(matrix[x][y])                       #Append current element to result.
                nx = x + 1 if i % 2 else x - 1                    #Calculate next value of x; if i is odd, increase x to move to next row, otherwise decrease x to move to previous row.
                ny = y - 1 if i % 2 else y + 1                    #Calculate next value of y; if i is odd, decrease y to move to previous column, otherwise increase y to move to next column.
                if nx < 0 or nx == m or ny < 0 or ny == n:        #If nx or ny is out of matrix boundary, break.
                    break
                x, y = nx, ny                                     #Replace x and y with nx and ny.
            if (x == 0 and y < n - 1) or x == m - 1:              #If current position is on upper boundary(exculde the top right corner) or lower boundary, move to the next column.
                y += 1
            else:                                                 #Otherwise move to next row.
                x += 1
                
        return result
