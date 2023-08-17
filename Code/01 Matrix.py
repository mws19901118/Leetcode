class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])                                                                                                          #Get demensions of mat.
        distance = [[0 for _ in range(n)] for _ in range(m)]                                                                                  #Create distance matrix with same dimensions.
        q = []                                                                                                                                #Initialize queue.
        for i, j in product(range(m), range(n)):                                                                                              #Traverse mat.
            if mat[i][j] == 0:
                continue
            if any(0 <= x < m and 0 <= y < n and mat[x][y] == 0 for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]):                #If current cell is 1 and has neighbor who is 0, add current cell to q and set its distance to be 1.
                q.append((i, j))
                distance[i][j] = 1
            else:                                                                                                                             #If current cell is 1 and has no neighbors who is 0, set current cell to be -1.
                distance[i][j] = -1
        while q:                                                                                                                              #BFS.
            newq = []                                                                                                                         #Initialize new queue.
            for i, j in q:                                                                                                                    #For each cell in q, traverse the 4 neighbors.
                for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                    if 0 <= x < m and 0 <= y < n and distance[x][y] == -1:                                                                    #If neighbor is valid and has distance -1, set it to be distance of current cell plus 1 and append neightbor to newq.
                        distance[x][y] = distance[i][j] + 1
                        newq.append((x, y))
            q = newq                                                                                                                          #Replace q with newq.
        return distance                                                                                                                       #Return distance.
