class Solution:
    def backtrack(self, board, blank, row, column, square, index):
        if index==len(blank):                                                                                                       #If current index equals the length of blank, backtracking reaches the end and a possible solution is found.
            return True
        x=blank[index][0]                                                                                                           #Get the coordinate of current position.
        y=blank[index][1]
        for i in range(9):
            c=str(i+1)                                                                                                              #Traverse from 1 to 9.
            if row[x][c]==True or column[y][c]==True or square[x/3*3+y/3][c]==True:                                                 #if current digit contradicts with other digits, jump over it.
                continue
            else:
                board[x][y]=c                                                                                                       #If current digit is avaliable, update the sudoku board and dicts.
                row[x][c]=True
                column[y][c]=True
                square[x/3*3+y/3][c]=True
                if self.backtrack(board, blank, row, column, square, index+1)==True:                                                #Backtrack at next element index of blank. If the result is true, a possible solution is found, then return true.
                    return True
                else:
                    board[x][y]='.'                                                                                                 #If can't find a possible solution, recover the sudoku board and dicts.
                    row[x][c]=False
                    column[y][c]=False
                    square[x/3*3+y/3][c]=False
        return False                                                                                                                #If all the digits from 1 to 9 is not valid at this position, return false.
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solveSudoku(self, board):
        row=[{'1':False,'2':False,'3':False,'4':False,'5':False,'6':False,'7':False,'8':False,'9':False} for i in range(9)]         #Record the dicts for every row.
        column=[{'1':False,'2':False,'3':False,'4':False,'5':False,'6':False,'7':False,'8':False,'9':False} for i in range(9)]      #Record the dicts for every column.
        square=[{'1':False,'2':False,'3':False,'4':False,'5':False,'6':False,'7':False,'8':False,'9':False} for i in range(9)]      #Record the dicts for every little square.
        blank=[]                                                                                                                    #Record the avaliable coordinates.
        for i in range(9):
            for j in range(9):
                c=board[i][j]
                if c=='.':
                    blank.append((i,j))                                                                                             #If c is avaliable position, append the coordinate to blank.
                else:                                                                                                               #Initialize the dicts.
                    row[i][c]=True
                    column[j][c]=True
                    square[i/3*3+j/3][c]=True
        self.backtrack(board, blank, row, column, square, 0)                                                                        #Begin backtracking at the first element of blank.
