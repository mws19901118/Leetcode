class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):                                               #Simple dynamic programming
        m=len(grid)
        if m==0:
            return 0
        n=len(grid[0])
        if n==0:
            return 0
        minSum=[[0 for i in range(n) ] for j in range(m)]
        minSum[0][0]=grid[0][0]
        for i in range(1,m):
            minSum[i][0]=grid[i][0]+minSum[i-1][0]
        for i in range(1,n):
            minSum[0][i]=grid[0][i]+minSum[0][i-1]
        for i in range(1,m):
            for j in range(1,n):
                minSum[i][j]=min(minSum[i-1][j],minSum[i][j-1])+grid[i][j]
        return minSum[m-1][n-1]
