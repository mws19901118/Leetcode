class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        for i in range(1, len(grid)):                                                                                            #Iterate len(grid) - 1 times.
            smallestIndex, secondSmallestIndex = -1, -1                                                                          #Find the index of smallest and second smallest number in previous row.
            for j, x in enumerate(grid[i - 1]):                                                                                  #Traverse previous row.
                if smallestIndex == -1 or x <= grid[i - 1][smallestIndex]:                                                       #Update smallest index if it is not set or current number is not greater; then give last value to second smallest index.
                    smallestIndex, secondSmallestIndex = j, smallestIndex
                elif secondSmallestIndex == -1 or x <= grid[i - 1][secondSmallestIndex]:                                         #Update second smallest index if it is not set or current number is not greater but smaller than the smallest number.
                    secondSmallestIndex = j
            for j in range(len(grid[i])):                                                                                        #Traverse current row.
                grid[i][j] += grid[i - 1][smallestIndex] if j != smallestIndex else grid[i - 1][secondSmallestIndex]             #If the index is same as smallest index, add the number on second smallest index of previous row; otherwise add the number on smallest index of previous row.
        return min(grid[-1])                                                                                                     #Return the smallest in last row.
