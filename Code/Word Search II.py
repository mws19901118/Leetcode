class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        prefix = defaultdict(int)                                                           #Store the count of prefixes in words.
        wordPrefixes = defaultdict(list)                                                    #Store the prefixes of each word.
        for w in words:                                                                     #Traverse words.
            for i in range(len(w)):                                                         #Enumerate each prefix of w.
                p = w[0:i + 1]
                prefix[p] += 1                                                              #Increase count of p.
                wordPrefixes[w].append(p)                                                   #Append p to wordPrefixes[w].

        words = set(words)                                                                  #Store all words in set.
        found = []                                                                          #Store found words.
        visited = set()                                                                     #Store visited cells.
        m, n = len(board), len(board[0])                                                    #Get the dimensions of board.

        def dfs(x: int, y:int, w: str):                                                     #DFS.
            visited.add((x, y))                                                             #Add cell to visited.

            if w in words:                                                                  #If current word in words, add it to found and remove it from words.
                found.append(w)
                words.remove(w)
                for p in wordPrefixes[w]:                                                   #Decrease count of each its prefixes.
                    prefix[p] -= 1

            for nx, ny in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:                 #Traverse neighbor cells.
                if (nx, ny) in visited or not (0 <= nx < m and 0 <= ny < n):                #If neighbor is already visited or not valid, skip.
                    continue
                new_w = w + board[nx][ny]                                                   #Apeend character on neighbor to current word to get new word.
                if prefix[new_w] > 0:                                                       #If it is prefix of any word, keep dfs.
                    dfs(nx, ny, new_w)

            visited.remove((x, y))                                                          #Mark cell as unvisited.

        for i, j in product(range(m), range(n)):                                            #Starting DFS at each cell on board if it is prefix of any word.
            if board[i][j] in prefix:
                dfs(i, j, board[i][j])

        return found                                                                        #Return found.
