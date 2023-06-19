class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])                                                    #Get dimensions.
        division = 10 ** 9 + 7                                                            #Set division.

        @cache                                                                            #Cache result.
        def DFS(x: int, y: int) -> int:                                                   #DFS to find all the strictly increasing paths starting from current position. 
            result = 1                                                                    #Initialize result as itself is a path.
            for i, j in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:                 #Traverse all neighbors.
                if 0 <= i < m and 0 <= j < n and grid[x][y] < grid[i][j]:                 #If neighbor is greater than current position, add DFS(i, j) % divison to result.
                    result += DFS(i, j) % division
            return result                                                                 #Return result.

        return sum(DFS(i, j) for i, j in product(range(m), range(n))) % division          #Sum up count of paths starting at each position and return.
