class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        @cache                                                                                  #Cache result.
        def DFS(x: int, y:int) -> None:
            maxLength = 0
            for u, v in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:                       #Traverse 4 neighbors.
                if 0 <= u < m and 0 <= v < n and matrix[u][v] > matrix[x][y]:                   #If neighbor is valid and larger than current value, keep DFS and update result.
                    maxLength = max(maxLength, DFS(u, v))
            return maxLength + 1                                                                #Return maxLength + 1.

        m, n = len(matrix), len(matrix[0])                                                      #Return result.
        return max(DFS(i, j) for i, j in product(range(m), range(n)))                           #Traverse matrix and start DFS at each position and return max result.
