class Solution:
    def dfs(self, x: int, n: int, board: List[List[str]], column: List[int], diagonal1: List[int], diagonal2: List[int], solutions: List[List[str]]) -> None:
        if x == n:                                                                                                                                                  #If DFS has finished last row, we found a solution.
            solutions.append(["".join(row) for row in board])                                                                                                       #Join each row and append the list of rows to solutions.
            return
        for y in range(n):                                                                                                                                          #Traverse each cell in current row.
            if not column[y] and not diagonal1[x + y] and not diagonal2[n - 1 - x + y]:                                                                             #If there is no queens in this column and 2 diagonals, we can place a queen here.
                board[x][y] = 'Q'
                column[y] += 1                                                                                                                                      #Update column, diagonal1 and diagonal2.
                diagonal1[x + y] += 1
                diagonal2[n - 1 - x + y] += 1
                self.dfs(x + 1, n, board, column, diagonal1, diagonal2, solutions)                                                                                  #DFS next row.
                board[x][y] = '.'                                                                                                                                   #Restore the board.
                column[y] -= 1
                diagonal1[x + y] -= 1
                diagonal2[n - 1 - x + y] -= 1
                
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for j in range(n)] for i in range(n)]                                                                                                         #Initialize empty board.
        column, diagonal1, diagonal2 = [0] * n, [0] * (2 * n - 1), [0] * (2 * n - 1)                                                                                #Initialize the number of queens in each column and diagonal(2 directions).
        solutions = []                                                                                                                                              #initialize solutions.
        self.dfs(0, n, board, column, diagonal1, diagonal2, solutions)                                                                                              #DFS from first row.
        return solutions
