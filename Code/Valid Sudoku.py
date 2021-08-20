class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, column, box = [{} for i in range(9)], [{} for i in range(9)], [{} for i in range(9)]           #Record the dicts for every row, column or box.
        for i, j in product(range(9), range(9)):                                                            #Traverse board.
            if board[i][j] == '.':                                                                          #If c is not digit, continue.
                continue
            c = board[i][j]
            if c in row[i] or c in column[j] or c in box[i // 3 * 3 + j // 3]:                              #If c is already in a row, a column or a box, return false.
                return False
            row[i][c] = column[j][c] = box[i // 3 * 3 + j // 3][c] = True                                   #Store c in corresponding row, column and box.
        return True                                                                                         #Return true at the end.
