class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        row=[{} for i in range(9)]                          #Record the dicts for every row.
        column=[{} for i in range(9)]                       #Record the dicts for every column.
        square=[{} for i in range(9)]                       #Record the dicts for every little square.
        for i in range(9):
            for j in range(9):
                c=board[i][j]
                if c=='.':                                  #If c is not digit, continue.
                    continue
                    
                if c in row[i]:                             #If c is already in a row, return false; otherwise, store c in correspoding row dict.
                    return False
                else:
                    row[i][c]=True
                    
                if c in column[j]:                          #If c is already in a column, return false; otherwise, store c in correspoding column dict.
                    return False
                else:
                    column[j][c]=True
                
                if c in square[i/3*3+j/3]:                  #If c is already in a little square, return false; otherwise, store c in correspoding little square dict.
                    return False
                else:
                    square[i/3*3+j/3][c]=True
        return True                                         #If there is no conflicts, return true.
