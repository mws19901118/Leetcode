class Solution:
    def find(self, board: List[List[str]], x: int, y: int, visited: set, word: str) -> bool:
        if board[x][y] != word[0]:                                                                                                                  #If board[x][y] != word[0], return false.
            return False
        if len(word) == 1:                                                                                                                          #If len(word) == 1, we have found the word, return true.
            return True
        m, n = len(board), len(board[0])                                                                                                            #Get dimensions.
        result = False                                                                                                                              #Initialize result.
        visited.add((x, y))                                                                                                                         #Add (x, y) to visited.
        for nx, ny in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:                                                                             #Traverse 4 neighbors.
            result |= (nx >= 0 and nx < m and ny >= 0 and ny < n and (nx, ny) not in visited and self.find(board, nx, ny, visited, word[1:]))       #If neightbor is valid and unvisited, search word[1:] starting from neighbor and update result.
        visited.remove((x, y))                                                                                                                      #Remove (x, y) from visited.
        return result                                                                                                                               #Return result.

    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])                                                                                                            #Get dimensions.
        result = False                                                                                                                              #Initialize result.
        for i, j in product(range(m), range(n)):                                                                                                    #Traverse board.
            result |= self.find(board, i, j, set(), word)                                                                                           #Searching word starting from current cell and update result.
        return result                                                                                                                               #Return result.
