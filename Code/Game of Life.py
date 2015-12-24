class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        if n == 0:
            return
        for i in range(m):                                                                                        #In first traverse, mark each cell.
            for j in range(n):
                count = 0                                                                                         #Count the alive neighbors.
                for x, y in [(-1,-1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:                #Check all the 8 neighbors.
                    if i + x >= 0 and i + x < m and j + y >= 0 and j + y < n and board[i + x][j + y] % 2 == 1:    #If the neighbor is valid and it's alive, add 1 to count.
                        count += 1
                if board[i][j] == 1:
                    if count < 2 or count > 3:
                        board[i][j] = 3                                                                           #Use 3 to indicate cell which is alive in current state but should be dead in next state.
                else:
                    if count == 3:
                        board[i][j] = 2                                                                           #Use 2 to indicate cell which is dead in current state but should be alive in next state.
        for i in range(m):                                                                                        #In second traverse, change each cell acoording to the mark.
            for j in range(n):
                if board[i][j] == 3:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1
