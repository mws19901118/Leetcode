class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [['', '', ''], ['', '', ''], ['', '', '']]                                                                                                                                                                                                  #Initialize board.
        for i, m in enumerate(moves):                                                                                                                                                                                                                       #Place moves on board.
            board[m[0]][m[1]] = 'O' if i & 1 else 'X'
        if any(all(board[i][j] == 'X' for j in range(3)) for i in range(3)) or any(all(board[j][i] == 'X' for j in range(3)) for i in range(3)) or all(board[i][i] == 'X' for i in range(3)) or all(board[2 - i][i] == 'X' for i in range(3)):              #Check if there are 3 X filling any row, column, or diagonal; if so, A wins.
            return 'A'
        elif any(all(board[i][j] == 'O' for j in range(3)) for i in range(3)) or any(all(board[j][i] == 'O' for j in range(3)) for i in range(3)) or all(board[i][i] == 'O' for i in range(3)) or all(board[2 - i][i] == 'O' for i in range(3)):            #Check if there are 3 O filling any row, column, or diagonal; if so, B wins.
            return 'B'
        elif len(moves) == 9:                                                                                                                                                                                                                               #If no one wins, and the game is draw if moves already filled the board.
            return 'Draw'
        else:                                                                                                                                                                                                                                               #Otherwise, the game is still pending.
            return 'Pending'
