class TicTacToe:

    def __init__(self, n: int):
        self.n = n                                                                                                                                          #Store n.
        self.rows = [0] * n                                                                                                                                 #Store moves in each row.
        self.cols = [0] * n                                                                                                                                 #Store moves in each column.
        self.diagonal = 0                                                                                                                                   #Store moves in diagonal.
        self.antidiagonal = 0                                                                                                                               #Store moves in antidiagonal.

    def move(self, row: int, col: int, player: int) -> int:
        currentPlayer = 1 if player == 1 else -1                                                                                                            #Determine current player, 1 for player 1 and -1 for player 2.
        self.rows[row] += currentPlayer                                                                                                                     #Update moves in current row.
        self.cols[col] += currentPlayer                                                                                                                     #Update moves in current column.
        if row == col:                                                                                                                                      #Update moves in diagonal if current move is in diagonal.
            self.diagonal += currentPlayer
        if row + col == self.n - 1:                                                                                                                         #Update moves in antidiagonal if current move is in antidiagonal.
            self.antidiagonal += currentPlayer
        return player if any(abs(x) == self.n for x in [self.rows[row], self.cols[col], self.diagonal, self.antidiagonal]) else 0                           #Return current player if any of current row, current column, diagonal and antidiagonal is all occupied by current player; otherwise return 0.

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
