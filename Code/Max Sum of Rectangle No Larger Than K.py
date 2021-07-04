class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])                                              #Get dimensions. 
        result = -1000001                                                               #Initialize result to be the smaller than the possible minimum value.
        rowPrefixSum = [[0] * (n + 1) for _ in range(m)]                                #Initialize prefix sum of each row.
        for col1 in range(n):                                                           #Enumerate the right edge column of rectangle in matrix.
            for i in range(m):                                                          #For each row, update the prefix sum till col1.
                rowPrefixSum[i].append(matrix[i][col1] + rowPrefixSum[i][-1])
            for col2 in range(col1 + 1):                                                #Enumerate the left edge column of rectangle in matrix. So, within this loop, 2 edge columns are fixed. 
                prefixSum, values = 0, [0]                                              #Initialize current prefix sum and the sorted list of traversed prefix sum while traversing rows from top to bottom.
                for i in range(m):                                                      #Traverse the bottom row of rectangle in matrix.
                    prefixSum += rowPrefixSum[i][col1 + 1] - rowPrefixSum[i][col2]      #Compute the current prefix sum.
                    x = bisect_left(sortedPrefixSum, prefixSum - k)                     #Bianry search the position of prefixSum - k in sorted list of traversed prefix sum.
                    if x < len(sortedPrefixSum):                                        #So, if x is valid, sortedPrefixSum[x] is the smallest prefix sum that satisfies sortedPrefixSum[x] >= prefixSum - k, i, e. k >= prefixSum - sortedPrefixSum[x].
                        result = max(result, prefixSum - sortedPrefixSum[x])            #Thus, the corresponding row of sortedPrefixSum[x] is the top edge row of rectangle sum no larger than k with given edge columns and bottom edge row. Update result if necessary.
                    insort_left(sortedPrefixSum, prefixSum)                             #Insert current prefix sum to the sorted list of traversed prefix sum and keep the list sorted.
        return result                                                                   #Return result.
