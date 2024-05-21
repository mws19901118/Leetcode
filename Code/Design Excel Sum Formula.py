class Excel:

    def __init__(self, height: int, width: str):
        self.matrix = [[0 for _ in range(self.getColumnIndex(width) + 1)] for _ in range(height)]                                                            #Initialize matrix.
        self.contribution = defaultdict(Counter)                                                                                                             #For each cell, store the multipler it contributes to each sum formula.
        self.contributor = defaultdict(list)                                                                                                                 #For each sum formula, store the contributor cells.

    def set(self, row: int, column: str, val: int) -> None:
        rowIndex, columnIndex = self.getRowIndex(row), self.getColumnIndex(column)                                                                           #Get the row index and column index.
        self.clearSum(rowIndex, columnIndex)                                                                                                                 #Clear the contributions for the sum at current cell.
        delta = val - self.matrix[rowIndex][columnIndex]                                                                                                     #Compute delta.
        self.populate(rowIndex, columnIndex, delta)                                                                                                          #Populate delta to all the sum formula current cell contributes to.

    def get(self, row: int, column: str) -> int:
        return self.matrix[self.getRowIndex(row)][self.getColumnIndex(column)]                                                                               #Return the value at current row index and column index.

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        rowIndex, columnIndex = self.getRowIndex(row), self.getColumnIndex(column)                                                                           #Get the row index and column index.
        self.clearSum(rowIndex, columnIndex)                                                                                                                 #Clear the contributions for the sum at current cell.
        val = 0                                                                                                                                              #Initialize sum value.
        contributionCount = Counter()                                                                                                                        #Initialize the contribution for each cell.
        for x in numbers:                                                                                                                                    #Traverse numbers.
            index = x.find(":")                                                                                                                              #Find ':' in number.
            if index == -1:                                                                                                                                  #If not found, x is a cell.
                xRowIndex, xColIndex = self.getRowIndex(int(x[1:])), self.getColumnIndex(x[0])                                                               #Get its row index and column index.
                val += self.matrix[xRowIndex][xColIndex]                                                                                                     #Add its value to sum value.
                contributionCount[(xRowIndex, xColIndex)] += 1                                                                                               #Increase its contribution by 1.
            else:                                                                                                                                            #If found, x is a rectangle.
                topLeftRowIndex, topLeftColumnIndex = self.getRowIndex(int(x[1:index])), self.getColumnIndex(x[0])                                           #Get the row index and column index of top left cell.
                bottomRightRowIndex, bottomRightColumnIndex = self.getRowIndex(int(x[index + 2:])), self.getColumnIndex(x[index + 1])                        #Get the row index and column index of bottom right cell.
                for i, j in product(range(topLeftRowIndex, bottomRightRowIndex + 1), range(topLeftColumnIndex, bottomRightColumnIndex + 1)):                 #Traverse the rectangle.
                    val += self.matrix[i][j]                                                                                                                 #Add each value to sum value.
                    contributionCount[(i, j)] += 1                                                                                                           #Increase each contribution by 1.
        self.contributor[(rowIndex, columnIndex)] = contributionCount.keys()                                                                                 #Update the contributors of current sum.
        for x, y in contributionCount.keys():                                                                                                                #Traverse the contributors.
            self.contribution[(x, y)][(rowIndex, columnIndex)] += contributionCount[(x, y)]                                                                  #Update contribution for each cell.
        delta = val - self.matrix[rowIndex][columnIndex]                                                                                                     #Compute delta.
        self.populate(rowIndex, columnIndex, delta)                                                                                                          #Populate delta to all the sum formula current cell contributes to.
        return val                                                                                                                                           #Return delta

    def getColumnIndex(self, column: str) -> int:
        return ord(column) - ord('A')                                                                                                                        #Compute the column index from column.
    
    def getRowIndex(self, row: int) -> int:
        return row - 1                                                                                                                                       #Compute the row index from row.
    
    def clearSum(self, rowIndex: int, columnIndex: str) -> None:
        for x, y in self.contributor[(rowIndex, columnIndex)]:                                                                                               #Traverse all cells that contributes to current sum.
            self.contribution[(x, y)].pop((rowIndex, columnIndex))                                                                                           #Pop its contribution to current sum.
        self.contributor.pop((rowIndex, columnIndex))                                                                                                        #Pop all cells that contributes to current sum

    def populate(self, rowIndex: int, columnIndex: int, delta: int) -> None:
        self.matrix[rowIndex][columnIndex] += delta                                                                                                          #Add delta to the cell at row index and column index.
        for (x, y), multiplier in self.contribution[(rowIndex, columnIndex)].items():                                                                        #Traverse contributions of current cell.
            self.populate(x, y, multiplier * delta)                                                                                                          #Recursively update target with multiplied delta.

# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)
