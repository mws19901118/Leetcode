class Solution(object):
    def DFS(self, matrix, lip, x, y):
        m = len(matrix)
        n = len(matrix[0])
        if lip[x][y] != 0:                                                                  #If current position has been DFSed, directly return the result.
            return lip[x][y]
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:                                   #Check 4 directions.
            nx = x + dx
            ny = y + dy
            if nx >= 0 and nx < m and ny >= 0 and ny < n and matrix[nx][ny] > matrix[x][y]: #If the direction is valid and its value is greater than current value, do DFS at that direction and keep the max length.
                lip[x][y] = max(lip[x][y], self.DFS(matrix, lip, nx,ny))
        lip[x][y] += 1                                                                      #Increase current length by 1 for itself is the beginning of the path.
        return lip[x][y]                                                                    #Return the length of longest increasing path starting at current position.
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0
        lip = [[0 for j in range(n)] for i in range(m)]                                     #Record the length of longest increasing path starting at each position.
        maxlip = 0
        for i in range(m):
            for j in range(n):
                maxlip = max(maxlip, self.DFS(matrix, lip, i, j))                           #DFS at each position and keep the max length.
        return maxlip
