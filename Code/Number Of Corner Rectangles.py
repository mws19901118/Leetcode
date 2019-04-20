class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])                              #Get the dimensions of grid.
        pair = [[0 for i in range(n)] for i in range(n)]            #For a pair of columns, count the number of rows that have 1 on cell of those 2 columns.
        count = 0                                                   #Initialize count to be 0.
        for row in grid:                                            #Iterate through each row.
            indexes = []                                            #Store the indexes of cell 1.
            for i in range(len(row)):                               #For each index i of column in row.
                if row[i] == 1:                                     #If current cell is 1.
                    for j in indexes:                               #For each index j in indexes, add pair[j][i] to count, which is the number of corner rectangles whose bottom 2 corners are row[j] and row[i].
                        count += pair[j][i]
                        pair[j][i] += 1                             #Increase pair[j][i] by 1.
                    indexes.append(i)                               #Add i to indexes.
        return count                                                #Return count.
            
