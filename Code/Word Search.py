class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def find(x: int, y: int, word: str) -> bool:
            if board[x][y] != word[0]:                                                                                  #If board[x][y] != word[0], return false.
                return False
            if not word[1:]:                                                                                            #If word[1:] is empty, we have found the word, return true.
                return True
            t = board[x][y]                                                                                             #Store board[x][y] temporarily.
            board[x][y] = '.'                                                                                           #Set board[x][y] to mark it as visited.
            for i, j in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:                                               #Traverse 4 neighbors.
                if (0 <= i < m and 0 <= j < n and board[i][j] != '.' and find(i, j, word[1:])):                         #If neightbor is valid and unvisited, search word[1:] starting from neighbor and return true if found.
                    return True
            board[x][y] = t                                                                                             #Restore board[x][y].
            return False                                                                                                #Return false if not found.

        m, n = len(board), len(board[0])                                                                                #Get dimensions.
        return any(find(i, j, word) for i, j in product(range(m), range(n)))                                            #Return if the word can be found.
