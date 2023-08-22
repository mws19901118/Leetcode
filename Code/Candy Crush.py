class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m, n = len(board), len(board[0])                                            #Get dimensions.
        crush = True                                                                #Indicate if there is crush in current iteration; initially set to true to start loop.
        while crush:                                                                #Iterate.
            crush = False                                                           #New iteration start with no crush.
            for i in range(m):                                                      #Find crush in each row.
                j = 0
                while j < n:
                    if board[i][j] == 0:                                            #Skip current cell if it's zero.
                        j += 1
                        continue
                    k = j
                    while k < n and abs(board[i][j]) == abs(board[i][k]):           #Find consecutive cells with same value; use negative number because current cell can be part of other processed crush.
                        k += 1
                    if k - j >= 3:                                                  #If length is at least 3, there is a crush.
                        crush = True
                        for x in range(j, k):                                       #Set all cells in crush to negative number.
                            board[i][x] = -abs(board[i][j])
                    j = k
            for j in range(n):                                                      #Similarly, find crush in each column.
                i = 0
                while i < m:
                    if board[i][j] == 0:
                        i += 1
                        continue
                    k = i
                    while k < m and abs(board[i][j]) == abs(board[k][j]):
                        k += 1
                    if k - i >= 3:
                        crush = True
                        for x in range(i, k):
                            board[x][j] = -abs(board[i][j])
                    i = k
            
            for j in range(n):                                                      #In each row, drop down cells that are not part of crush.
                i, k = m - 1, m - 1                                                 #Use 2 pointers; i represents current cell to be dropped at and k represents current cell to drop.
                while k >= 0:
                    while k >= 0 and board[k][j] < 0:                               #Find next cell to drop(not negative).
                        k -= 1
                    if k >= 0:                                                      #If found, drop it from board[k][j] to board[i][j] and then decrease both i and k.
                        board[i][j] = board[k][j]
                        i -= 1
                        k -= 1
                    else:                                                           #Otherwise, break.
                        break
                while i >= 0:                                                       #Set rest cells in current column to zero.
                    board[i][j] = 0
                    i -= 1
        return board                                                                #Return board after no more crush.
