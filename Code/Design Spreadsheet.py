class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = [[0] * 26 for _ in range(rows)]                                                                    #Initialize spreedsheet.

    def setCell(self, cell: str, value: int) -> None:
        row, col = self.parse(cell)                                                                                     #Get the coordinate.
        self.sheet[row][col] = value                                                                                    #Update value.

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)                                                                                           #Set the cell to 0.

    def getValue(self, formula: str) -> int:
        part = formula[1:].split('+')                                                                                   #Get the 2 parts of add formula.
        part1 = int(part[0]) if part[0].isdigit() else self.sheet[self.parse(part[0])[0]][self.parse(part[0])[1]]       #Get the value of part1; if the string is digit, convert it to int; otherwise get the value at corresponding reference.
        part2 = int(part[1]) if part[1].isdigit() else self.sheet[self.parse(part[1])[0]][self.parse(part[1])[1]]       #Get the value of part2; if the string is digit, convert it to int; otherwise get the value at corresponding reference.
        return part1 + part2                                                                                            #Return the sum.

    @cache
    def parse(self, cell: str) -> (int, int):
        return int(cell[1:]) - 1, ord(cell[0]) - ord('A')                                                               #Parse cell reference.

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
