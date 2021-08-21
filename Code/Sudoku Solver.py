class Solution:
    def dfs(self, board: List[List[str]], cells: List[tuple], row: List[dict], column: List[dict], box: List[dict]) -> bool:
        if not cells:                                                                                                                   #If cells is empty, a solution is found, so return true.
            return True
        i, j = cells[0]                                                                                                                 #Get the coordinate of cells[0].
        for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:                                                                                           #Traverse from 1 to 9.
            if row[i][x] or column[j][x] or box[i // 3 * 3 + j // 3][x]:                                                                #If x is already in corresponding row, column or box, continue.
                continue
            board[i][j] = str(x)                                                                                                        #Set board[i][j] tp str(x).
            row[i][x] = column[j][x] = box[i // 3 * 3 + j // 3][x] = True                                                               #Update x in corresponding row, column and box.
            if self.dfs(board, cells[1:], row, column, box):                                                                            #Keep filling sudoku; if a solution is found, return true.
                return True
            row[i][x] = column[j][x] = box[i // 3 * 3 + j // 3][x] = False                                                              #Reset x in corresponding row, column and box.
        return False                                                                                                                    #Return false after traverse because of no solution found.
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, column, box = [[False] * 10 for i in range(9)], [[False] * 10 for i in range(9)], [[False] * 10 for i in range(9)]         #Record if each number is filled for every row, column or box.
        cells = []                                                                                                                      #Store unfilled cells.
        for i, j in product(range(9), range(9)):                                                                                        #Traverse board.                
            if board[i][j] == '.':                                                                                                      #If x is not digit, append coordinate to cells and continue.
                cells.append((i, j))
                continue
            x = int(board[i][j])                                                                                                        #Convert board[i][j] to int.
            row[i][x] = column[j][x] = box[i // 3 * 3 + j // 3][x] = True                                                               #Update x in corresponding row, column and box.
        self.dfs(board, cells, row, column, box)                                                                                        #Fill sudoku.
