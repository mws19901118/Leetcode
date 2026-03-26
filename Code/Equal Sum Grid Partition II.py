class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def isValidPartition(topSum: int, bottomSum: int, topCount: Counter, bottomCount: Counter) -> bool:                                                                                                    #Determine if current partition is valud based on topSum, bottomSum, topCount and bottomCount.
            return topSum == bottomSum or topCount[topSum - bottomSum] or bottomCount[bottomSum - topSum]                                                                                                      #Partition is valid if either topSum equals bottomSum or topSum - bottomSum has a positive count(discount 1 cell in top) in topCount or bottomSum - topSum has a positive count(discount 1 cell in bottom) in bottomCount.

        def horizontalPartition(matrix: List[List[int]]) -> bool:                                                                                                                                              #Determine if matrix can be horizontally partitioned.
            m, n = len(matrix), len(matrix[0])                                                                                                                                                                 #Get the dimensions.
            total = sum(sum(row) for row in matrix)                                                                                                                                                            #Calculate total sum.
            
            if n == 1:                                                                                                                                                                                         #Handle the case that the matrix only has 1 column.
                topCount, bottomCount = Counter(), Counter([matrix[0][0], matrix[-1][0]])                                                                                                                      #Initialize the top count with empty counter and the bottom count with the top cell and the bottom cell.
                prefixSum = 0                                                                                                                                                                                  #Initialize the prefix sum.
                for i, row in enumerate(matrix[:m - 1]):                                                                                                                                                       #Traverse the top m - 1 rows.
                    prefixSum += row[0]                                                                                                                                                                        #Add current cell to the prefix sum.
                    topCount[row[0]] += 1                                                                                                                                                                      #Add current cell to the top count.
                    if i > 1:                                                                                                                                                                                  #If i > 1, remove the cell in last row from top count as it will disconnect the top partition.
                        topCount[matrix[i - 1][0]] -= 1
                    bottomCount[row[0]] -= 1                                                                                                                                                                   #Remove current cell from bottom count.
                    if i < m - 2:                                                                                                                                                                              #If i < m - 2, add the cell in next row to bottom count as it would be the upper boundary of bottom partition.
                        bottomCount[matrix[i + 1][0]] += 1
                    if isValidPartition(prefixSum, total - prefixSum, topCount, bottomCount):                                                                                                                  #If current partition is valid, return true.
                        return True
            else:                                                                                                                                                                                              #Handle the case that the matrix has multiple columns.
                topCount, bottomCount = Counter([matrix[0][0], matrix[0][-1]]), Counter(matrix[i][j] for i, j in product(range(1, m), range(n))) if m > 2 else Counter([matrix[-1][0], matrix[-1][-1]])        #Initialize the top count with the 2 top corners; also initialize botton count with the 2 bottom corners if m < 2 or the whole matrix except first row if m >= 2.
                prefixSum = sum(matrix[0])                                                                                                                                                                     #Initialize the prefix sum with the sum of first row.
                if isValidPartition(prefixSum, total - prefixSum, topCount, bottomCount):                                                                                                                      #Return true if first row is a valid partition.
                    return True
                for x in matrix[0][1:n - 1]:                                                                                                                                                                   #Add the rest of first row to top count.
                    topCount[x] += 1
                for i in range(1, m - 1):                                                                                                                                                                      #Traverse from the second row to the (m - 1)-th row.
                    prefixSum += sum(matrix[i])                                                                                                                                                                #Add the sum of current row to the prefix sum.
                    for x in matrix[i]:                                                                                                                                                                        #Traverse current row.
                        topCount[x] += 1                                                                                                                                                                       #Add current cell to top count.
                        bottomCount[x] -= 1                                                                                                                                                                    #Remove current cell from bottom count.
                    if i == m - 2:                                                                                                                                                                             #If i == m - 2, reset the bottom count with the 2 bottom corners.
                        bottomCount.clear()
                        bottomCount[matrix[-1][0]] += 1
                        bottomCount[matrix[-1][-1]] += 1
                    if isValidPartition(prefixSum, total - prefixSum, topCount, bottomCount):                                                                                                                  #If current partition is valid, return true.
                        return True
            return False                                                                                                                                                                                       #Return false at the end.

        m, n = len(grid), len(grid[0])                                                                                                                                                                         #Get the dimensions.
        transpose = [[grid[i][j] for i in range(m)] for j in range(n)]                                                                                                                                         #Construct the transposed grid.
        return partition(grid) or partition(transpose)                                                                                                                                                         #Return either grid or transposed grid can be partitioned.
