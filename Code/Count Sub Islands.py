class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])                                                  #Get the dimensions.
        label = -1                                                                        #Initialize a label for each island.
        for i, j in product(range(m), range(n)):                                          #Traverse grid1.
            if grid1[i][j] == 1:                                                          #BFS to traverse each island and assign each cell the same label.
                grid1[i][j] = label
                dq = deque([(i, j)])
                while dq:
                    x, y = dq.popleft()
                    for u, v in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:
                        if 0 <= u < m and 0 <= v < n and grid1[u][v] == 1:
                            grid1[u][v] = label
                            dq.append((u, v))
                label -= 1                                                                #Decrease label.
        count, label = 0, -1                                                              #Initialize count.
        for i, j in product(range(m), range(n)):                                          #Do the same thing for grid2.
            if grid2[i][j] == 1:
                grid1Label, isSubIsland = grid1[i][j], grid1[i][j] < 0                    #Get the label of i, j in grid1 and make sure it is island.
                grid2[i][j] = label
                dq = deque([(i, j)])
                while dq:
                    x, y = dq.popleft()
                    for u, v in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:
                        if 0 <= u < m and 0 <= v < n and grid2[u][v] == 1:
                            grid2[u][v] = label
                            dq.append((u, v))
                            isSubIsland &= grid1[u][v] == grid1Label                      #If for any u, v, the corresponding label in grid1 is not same as grid1Label, current island is not sub island.
                label -= 1
                count += int(isSubIsland)                                                 #Add 1 if is sub island.
        return count
