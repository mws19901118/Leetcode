class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):               #Simple dynamic programming. If encounter a obstacle, set the number of paths in current coordinate to 0.
        m=len(obstacleGrid)
        if m==0:
            return 0
        n=len(obstacleGrid[0])
        if n==0:
            return 0
        minSum=[[0 for i in range(n) ] for j in range(m)]
        minSum[0][0]=1
        if obstacleGrid[0][0]==1:
                minSum[0][0]=0
        for i in range(1,m):
            minSum[i][0]=minSum[i-1][0]
            if obstacleGrid[i][0]==1:
                minSum[i][0]=0
        for i in range(1,n):
            minSum[0][i]=minSum[0][i-1]
            if obstacleGrid[0][i]==1:
                minSum[0][i]=0
        for i in range(1,m):
            for j in range(1,n):
                minSum[i][j]=minSum[i-1][j]+minSum[i][j-1]
                if obstacleGrid[i][j]==1:
                    minSum[i][j]=0
        return minSum[m-1][n-1]
