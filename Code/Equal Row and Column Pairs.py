class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n, count = len(grid), 0                           #Get dimension and initialize count.
        rowCounter = Counter(tuple(x) for x in grid)      #Convert each row into tuple and count them.
        for i in range(n):                                #Traverse each column.
            column = [grid[j][i] for j in range(n)]       #Convert the column into tuple.
            count += rowCounter[tuple(column)]            #Add the count of the same tuple in rowCounter to count.
        return count                                      #Return count.
