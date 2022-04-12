class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])                                                                                                                                #Get demensions.
        for i, j in product(range(m), range(n)):                                                                                                                        #Traverse board.
            count = sum(board[x][y] & 1 for x, y in product([i - 1, i, i + 1], [j - 1, j, j + 1]) if 0 <= x < m and 0 <= y < n and (x != i or y != j))                  #Count the alive neighbors.
            if board[i][j] and 2 <= count <= 3:                                                                                                                         #Use 3 to indicate cell which is alive in current state but should be dead in next state.
                board[i][j] = 3
            elif not board[i][j] and count == 3:                                                                                                                        #Use 2 to indicate cell which is dead in current state but should be alive in next state.
                board[i][j] = 2
        for i, j in product(range(m), range(n)):                                                                                                                        #Traverse board again and change each cell acoording to the new state.
            board[i][j] >>= 1
