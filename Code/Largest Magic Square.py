class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])                                                              #Get the dimensions.
        hPrefixSum = [[0] * (n + 1) for _ in range(m + 1)]                                          #Initialize horizontal prefix sum.
        vPrefixSum = [[0] * (n + 1) for _ in range(m + 1)]                                          #Initialize vertical prefix sum.
        dPrefixSum = [[0] * (n + 1) for _ in range(m + 1)]                                          #Initialize diagonal(from top left to bottom right) prefix sum.
        rdPrefixSum = [[0] * (n + 1) for _ in range(m + 1)]                                         #Initialize reverse diagonal(from top right to bottom left) prefix sum.
        for i, j in product(range(m), range(n)):                                                    #Traverse grid.
            hPrefixSum[i + 1][j + 1] = hPrefixSum[i + 1][j] + grid[i][j]                            #Populate horizontal prefix sum
            vPrefixSum[i + 1][j + 1] = vPrefixSum[i][j + 1] + grid[i][j]                            #Populate vertical prefix sum
            dPrefixSum[i + 1][j + 1] = dPrefixSum[i][j] + grid[i][j]                                #Populate diagonal prefix sum
            rdPrefixSum[i + 1][j] = rdPrefixSum[i][j + 1] + grid[i][j]                              #Populate reverse diagonal prefix sum
        result = 0
        for i, j in product(range(m), range(n)):                                                    #Traverse grid again.
            for k in range(1, min(i + 1, j + 1) + 1):                                               #Enumerate the possible side length of squares whose bottom right corner is grid[i][j].
                s = set()                                                                           #Store the row, column, diagonal and reverse diagonal sums in a set.
                for l in range(k):                                                                  #Traverse from 0 to k - 1.
                    s.add(hPrefixSum[i + 1 - l][j + 1] - hPrefixSum[i + 1 - l][j - k + 1])          #Add the sum of each row in square to s.
                    s.add(vPrefixSum[i + 1][j + 1 - l] - vPrefixSum[i - k + 1][j + 1 - l])          #Add the sum of each column in square to s.
                s.add(dPrefixSum[i + 1][j + 1] - dPrefixSum[i + 1 - k][j + 1 - k])                  #Add the sum of diagonal in square to s.
                s.add(rdPrefixSum[i + 1][j + 1 - k] - rdPrefixSum[i + 1 - k][j + 1])                #Add the sum of reverse diagonal in square to s.
                if len(s) == 1:                                                                     #If the length of s is 1, meaning all row, column, diagonal and reverse diagonal sums are equal.
                    result = max(result, k)                                                         #Thus, the square whose bottom right corner is grid[i][j] with length k is a magic sqaure; update result if necessary.
        return result
