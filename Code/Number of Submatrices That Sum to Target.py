class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])                                      #Get the dimemsions of matrix.
        prefixSum = [[0 for j in range(n + 1)] for i in range(m)]               #Store the prefix sum of each row.
        for i, j in product(range(m), range(n)):
            prefixSum[i][j + 1] = prefixSum[i][j] + matrix[i][j]
        count = 0
        for i in range(n):                                                      #Check every combination of left end column and right end column.
            for j in range(i, n):
                currentSum = 0                                                  #Track the sum of submatrix whose left end column and right end column is given and top row is the first row while bottom row is scanning from top to bottom.
                accumulation = defaultdict(int)                                 #Store the number of occurrence of given sum.
                accumulation[0] = 1                                             #Initially, the sum is 0.
                for k in range(m):                                              #Scanning bottom row from top to bottom.
                    currentSum += prefixSum[k][j + 1] - prefixSum[k][i]         #Update sum by adding the sum of current bottom row.
                    count += accumulation[currentSum - target]                  #If a currentSum - target value already in accumulation, there is a submatrix whose sum is target. So, add accumulation[currentSum - target] to count.
                    accumulation[currentSum] += 1                               #Update accumulation.
        return count
