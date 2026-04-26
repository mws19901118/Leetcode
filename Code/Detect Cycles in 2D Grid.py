class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        def dfs(x: int, y: int, prevX: int, prevY: int, currVisited: set):                                                                                                                                            #DFS to find cycle.
            if (x, y) in currVisited:                                                                                                                                                                                 #If (x, y) is in current visited, there is a cycle so return true.
                return True
    currVisited.add((x, y))                                                                                                                                                                                           #Add (x, y) to current visited.
            visited.add((x, y))                                                                                                                                                                                       #Add (x, y) to visited.
            return any(dfs(u, v, x, y, currVisited) for u, v in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)] if 0 <= u < m and 0 <= v < n and (u, v) != (prevX, prevY) and grid[u][v] == grid[x][y])              #Return true if can find cycle from the DFS towards any of the valid(not out of bounds, not same as previous cell, same cell value) neighbors.
        
        m, n = len(grid), len(grid[0])
        visited = set()
        return any(dfs(i, j, None, None, set()) for i, j in product(range(m), range(n)) if (i, j) not in visited)                                                                                                     #Return true if we can find cycle in any unvisited cell.
