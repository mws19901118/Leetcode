class Solution:
    def find(self, board: List[List[str]], x: int, y: int, word: str) -> bool:
        if board[x][y] != word[0]:                                                                                                                  #If board[x][y] != word[0], return false.
            return False
        if len(word) == 1:                                                                                                                          #If len(word) == 1, we have found the word, return true.
            return True
        m, n = len(board), len(board[0])                                                                                                            #Get dimensions.
        t = board[x][y]                                                                                                                             #Store board[x][y] temporarily.
        board[x][y] = '.'                                                                                                                           #Set board[x][y] to mark it as visited.
        for nx, ny in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:                                                                             #Traverse 4 neighbors.
            if (nx >= 0 and nx < m and ny >= 0 and ny < n and board[nx][ny] != '.' and self.find(board, nx, ny, word[1:])):                         #If neightbor is valid and unvisited, search word[1:] starting from neighbor and return true if found.
                return True
        board[x][y] = t                                                                                                                             #Restore board[x][y].
        return False                                                                                                                                #Return if not found.

    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])                                                                                                            #Get dimensions.
        for i, j in product(range(m), range(n)):                                                                                                    #Traverse board.
            if self.find(board, i, j, word):                                                                                                        #Searching word starting from current cell; if found then return true.
                return True
        return False                                                                                                                                #Return false if not found.
