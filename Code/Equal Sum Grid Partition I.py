class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])                              #Get the dimensions.
        total = sum(sum(row) for row in grid)                       #Calculate total sum.
        rowPrefixSum = 0
        for row in grid:                                            #Traverse each row from top to bottom.
            rowPrefixSum += sum(row)                                #Update row prefix sum.
            if rowPrefixSum == total - rowPrefixSum:                #If the grid is partitioned into 2 parts with equal sum, return true.
                return True
        columnPrefixSum = 0
        for j in range(n):                                          #Traverse each column from left to right.
            columnPrefixSum += sum(grid[i][j] for i in range(m))    #Update row prefix sum.
            if columnPrefixSum == total - columnPrefixSum:          #If the grid is partitioned into 2 parts with equal sum, return true.
                return True
        return False                                                #Return false at the end.
