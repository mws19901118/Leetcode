class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i in range(m):                                                                                          #In first traverse, mark each cell.
            for j in range(n):
                count = 0                                                                                           #Count the alive neighbors.
                for x, y in [(-1,-1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:                  #Check all the 8 neighbors.
                    if i + x >= 0 and i + x < m and j + y >= 0 and j + y < n and board[i + x][j + y] % 2 == 1:      #If the neighbor is valid and it's alive, add 1 to count.
                        count += 1
                if board[i][j] and count < 2 or count > 3:
                    board[i][j] = 3                                                                                 #Use 3 to indicate cell which is alive in current state but should be dead in next state.
                elif not board[i][j] and count == 3:
                    board[i][j] = 2                                                                                 #Use 2 to indicate cell which is dead in current state but should be alive in next state.
        for i in range(m):                                                                                          #In second traverse, change each cell acoording to the mark.
            for j in range(n):
                board[i][j] >>= 1
