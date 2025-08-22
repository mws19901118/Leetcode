class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])                          #Get the dimensions.
        min_x, min_y, max_x, max_y = m, n, 0, 0                 #Initialize min and max of x and y.
        for i, j in product(range(m), range(n)):                #Traverse grid.
            if not grid[i][j]:                                  #If grid[i][j] is 0, skip.
                continue
            min_x = min(min_x, i)                               #Update min_x.
            min_y = min(min_y, j)                               #Update min_y.
            max_x = max(max_x, i)                               #Update max_x.
            max_y = max(max_y, j)                               #Update max_y.
        return (max_x - min_x + 1) * (max_y - min_y + 1)        #The rectangle area is (max_x - min_x + 1) * (max_y - min_y + 1).
