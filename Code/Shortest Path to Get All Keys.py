class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])                                                                                                                    #Get the dimensions.
        keyMasks = {}                                                                                                                                     #Use a dict to store bit masks of key.
        mask, target = 1, 0                                                                                                                               #Initialize current mask and target bit mask.
        startPoint = None                                                                                                                                 #Initialize starting point.
        for i, j in product(range(m), range(n)):                                                                                                          #Traverse grid.
            if grid[i][j].islower():                                                                                                                      #If current cell is key, assign the mask to it.
                keyMasks[grid[i][j]] = mask
                target |= mask                                                                                                                            #Include current mask in target.
                mask <<= 1                                                                                                                                #Move to a new mask.
            elif grid[i][j] == "@":                                                                                                                       #Store the starting point.
                startPoint = (i, j)
        visitedKeyStates = defaultdict(set)                                                                                                               #Store all visited cells by the key state mask.
        visitedKeyStates[0].add(startPoint)                                                                                                               #Initially, key state with no key is visited by starting point.
        q = [(startPoint[0], startPoint[1], 0)]                                                                                                           #Initialize queue with starting point and starting key state, which is 0.
        moves = 0
        while q:                                                                                                                                          #BFS.
            newq = []                                                                                                                                     #Intialize new queue.
            for x, y, s in q:                                                                                                                             #Traverse queue.
                if s == target:                                                                                                                           #If current key state is target, we get all keys and return moves.
                    return moves
                for u, v in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:                                                                             #Traverse neighbors.
                    if 0 <= u < m and 0 <= v < n and grid[u][v] != '#' and not (grid[u][v].isupper() and not s & keyMasks[grid[u][v].lower()]):           #Process if neighbor is valid and not wall and not a lock that current key state cannot unlock.
                        ns = (s | keyMasks[grid[u][v]]) if grid[u][v].islower() else s                                                                    #New key state is same as current key state if neighbor is not key; otherwise include the key in new key state.
                        if (u, v) not in visitedKeyStates[ns]:                                                                                            #If neighbor is not visited in new key state, mark neighbor is visited in new key state and append neighbor and new key state to new queue.
                            visitedKeyStates[ns].add((u, v))
                            newq.append((u, v, ns))
            q = newq                                                                                                                                      #Replace q with newq.
            moves += 1
        return -1                                                                                                                                         #Return -1 if cannot get all keys.
