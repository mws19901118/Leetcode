class Solution:
    # @return an integer
    def uniquePaths(self, m, n):                                              #Simple dynamic programming
        if m==0 or n==0:
            return 0
        minSum=[[0 for i in range(n) ] for j in range(m)]
        minSum[0][0]=1
        for i in range(1,m):
            minSum[i][0]=1
        for i in range(1,n):
            minSum[0][i]=1
        for i in range(1,m):
            for j in range(1,n):
                minSum[i][j]=minSum[i-1][j]+minSum[i][j-1]
        return minSum[m-1][n-1]
