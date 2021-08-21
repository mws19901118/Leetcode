class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, column, box = [{} for i in range(9)], [{} for i in range(9)], [{} for i in range(9)]           #Record the dicts for every row, column or box.
        for i, j in product(range(9), range(9)):                                                            #Traverse board.
            if board[i][j] == '.':                                                                          #If x is not digit, continue.
                continue
            x = board[i][j]
            if x in row[i] or x in column[j] or x in box[i // 3 * 3 + j // 3]:                              #If x is already in a row, a column or a box, return false.
                return False
            row[i][x] = column[j][x] = box[i // 3 * 3 + j // 3][x] = True                                   #Store x in corresponding row, column and box.
        return True                                                                                         #Return true at the end.
