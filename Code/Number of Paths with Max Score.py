class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)                                                                      #Get the dimension.
        division = 10 ** 9 + 7                                                              #Initialize division.
        dp = [[[-1, 0] for _ in range(n)] for _ in range(n)]                                #Initialize dp(max score and number of paths) for each cell.
        dp[-1][-1] = [0, 1]                                                                 #For the bottom right corner, max score is 0 and number of paths is 1.
        for i, j in product(reversed(range(n)), reversed(range(n))):                        #Traverse the board from bottom to top, right to left.
            if (i, j) == (n - 1, n - 1) or board[i][j] == 'X':                              #If current cell is the botton right corner or is obstacle, skip.
                continue
            for x, y in [(i + 1, j), (i, j + 1), (i + 1, j + 1)]:                           #Traverse the 3 possible previous cells.
                if x >= n or y >= n or board[x][y] == 'X' or dp[x][y][0] == -1:             #If it is out of bound or is obstacle or is not reachable, skip.
                    continue
                score = dp[x][y][0] + (0 if board[i][j] == 'E' else int(board[i][j]))       #Calculate the score.
                if score > dp[i][j][0]:                                                     #If score is greater than max score, update max score and reset number of paths. 
                    dp[i][j][0] = score
                    dp[i][j][1] = 0
                if score == dp[i][j][0]:                                                    #If score equals max score, add the number of paths from previous cell.
                    dp[i][j][1] = (dp[i][j][1] + dp[x][y][1]) % division
        return [0, 0] if dp[0][0][0] == -1 else dp[0][0]                                    #Return [0, 0] if the top left corner is not reachable; otherwise, return dp[0][0].
