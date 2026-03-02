class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        last1 = []                                                 #Store the last index of 1 in each row.
        for row in grid:                                           #Traverse grid and populate last1.
            for j in reversed(range(len(grid))):
                if row[j]:
                    break
            last1.append(j)
        result = 0
        for i in range(len(grid)):                                 #Like selection sort, place each row from top to bottom.
            found = False
            for j in range(i, len(grid)):                          #Traverse from row i to the end.
                if last1[j] <= i:                                  #If current row has the last index of 1 not greater than i, it can be placed at current row.
                    result += j - i                                #Move row j to row i requires j - i operations.
                    for k in reversed(range(i + 1, j + 1)):        #Update the rows moved along the path.
                        last1[k] = last1[k - 1]
                    found = True                                   #Set found to true and break.
                    break
            if not found:                                          #If cannot find row for current row, return -1.
                return -1
        return result
