class Solution:
    def DFS(self, matrix: List[List[int]], length: List[List[int]], x: int, y: int) -> int:
        if length[x][y] > 0:                                                                    #If current position has been traversed, directly return the corresponding value stored.
            return length[x][y]
        m, n = len(matrix), len(matrix[0])                                                      #Get the dimensions.
        length[x][y] = 1                                                                        #Initialize length at 1.
        for nx, ny in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:                         #Traverse 4 neighbors.
            if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[x][y]:                   #If neighbor is valid and larger than current value, keep DFS and update length[x][y].
                length[x][y] = max(length[x][y], self.DFS(matrix, length, nx, ny) + 1)
        return length[x][y]                                                                     #Return length[x][y].
    
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])                                                      #Get the dimemsions.
        length = [[0 for j in range(n)] for i in range(m)]                                      #Store the longest increasing path length starting from each position in a 2D array, initially all 0.
        result = 0
        for i in range(m):                                                                      #Traverse matrix and start DFS at each position.
            for j in range(n):
                result = max(result, self.DFS(matrix, length, i, j))
        return result                                                                           #Return result.
