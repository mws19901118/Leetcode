class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])                      #Get the dimensions.
        perimeter = 0
        for i, j in product(range(m), range(n)):            #Traverse through grid.
            if grid[i][j] == 1:                             #If current cell is island, add 4 to perimeter.
                perimeter += 4
                if i - 1 >= 0 and grid[i - 1][j] == 1:      #If upper cell is island too, minus 2 from perimeter.
                    perimeter -= 2
                if j - 1 >= 0 and grid[i][j - 1] == 1:      #If left cell is island too, minus 2 from perimeter.
                    perimeter -= 2
        return perimeter
