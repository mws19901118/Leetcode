class Trie:
    def __init__(self):                                                                                                 #Initialize a trie node.
        self.words = {}
        self.hasValue = False
    
    def insert(self, word: str) -> None:                                                                                #Insert word to trie.
        if not word:
            self.hasValue = True
            return
        if word[0] not in self.words:
            self.words[word[0]] = Trie()
        self.words[word[0]].insert(word[1:])
            
class Solution:
    def dfs(self, result: List[str], trie: Trie, board: List[List[str]], x: int, y: int, word: str) -> None:            #DFS.
        c = board[x][y]                                                                                                 #Get current letter.
        if c not in trie.words:                                                                                         #If c is not in trie, return.
            return
        if trie.words[c].hasValue:                                                                                      #If c is in trie and there is word in trie ending at c, we found a word in board.
            result.append(word + c)                                                                                     #Append word + c to result.
            trie.words[c].hasValue = False                                                                              #Set trie.words[c].hasValue to false so we won't append duplicate words to result.
        m, n = len(board), len(board[0])                                                                                #Get dimensions.
        board[x][y] = '#'                                                                                               #Set board[x][y] to '#' meaning it's visited.
        for nx, ny in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:                                                 #Traverse neighbors.
            if nx >= 0 and nx < m and ny >= 0 and ny < n and board[nx][ny] != '#':                                      #If neighbor is valid and unvisited, keep dfs with trie.words[c] and word + c.
                self.dfs(result, trie.words[c], board, nx, ny, word + c)
        board[x][y] = c                                                                                                 #Restore board[x][y] to c.

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        t = Trie()                                                                                                      #Create a trie.
        for w in words:                                                                                                 #Insert each word in words to trie.
            t.insert(w)
        m, n = len(board), len(board[0])                                                                                #Get dimensions.
        result = []                                                                                                     #Initialize result.
        for i, j in product(range(m), range(n)):                                                                        #Traverse board.
            self.dfs(result, t, board, i, j, '')                                                                        #Search for word starting from current position.
        return result                                                                                                   #Return result.
