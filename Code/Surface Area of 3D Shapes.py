class Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        length = len(grid)
        width = len(grid[0])
        area = 0
        for i in range(length):
            heightX = 0                             #Record the height of cube tower in the previous cell of column.
            heightY = 0                             #Record the height of cube tower in the previous cell of row.
            for j in range(width):
                if grid[i][j]:                      #For each cube tower, both top and bottom contributes to surface area.
                    area += 2
                area += abs(grid[i][j] - heightX)   #Add the abs of height diff to surface area.
                heightX = grid[i][j]                #Update heightX.
                area += abs(grid[j][i] - heightY)   #Add the abs of height diff to surface area.
                heightY = grid[j][i]                #Update heightY.
            area += heightX                         #Add the height of last cell.
            area += heightY                         #Add the height of last cell.
        return area
