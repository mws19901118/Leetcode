class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        directions = {(-1, 1): (1, 1), (1, 1): (1, -1), (1, -1): (-1, -1), (-1, -1): (-1, 1)}                      #Initialize directions and every clockwise turn.
        m, n = len(grid), len(grid[0])                                                                             #Get the dimensions.

        @cache                                                                                                     #Cache result.
        def dfs(x: int, y: int, u: int, v: int, turn_allowed: bool, target: int):                                  #DFS.
            i, j = x + u, y + v                                                                                    #Get the next coordinate based on current coordinate and direction.
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != target:                                         #If next coordinate is invalid or not target, return 0 directly.
                return 0
            length = dfs(i, j, u, v, turn_allowed, 2 - target)                                                     #Keep DFS in current direction with the opposite of target.
            if turn_allowed:                                                                                       #If turn is allowed, turn clockwise and keep DFS with the opposite of target.
                length = max(length, dfs(i, j, directions[(u, v)][0], directions[(u, v)][1], False, 2 - target))
            return length + 1                                                                                      #Return length + 1 to include current element itself.

        result = 0
        for i, j in product(range(m), range(n)):                                                                   #Traverse grid.
            if grid[i][j] == 1:                                                                                    #If current element is 1, start to find. 
                for u, v in directions:                                                                            #Traverse all directions.
                    result = max(result, dfs(i, j, u, v, True, 2) + 1)                                             #Start DFS to find 2, then add 1 to result to include current element itself.
        return result
