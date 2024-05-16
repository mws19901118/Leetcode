class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])                                                                                                          #Get the dimensions.
        distance = [[inf for _ in range(n)] for _ in range(m)]                                                                                #Create distance matrix with same dimensions.
        q = []                                                                                                                                #Initialize queue.
        for i, j in product(range(m), range(n)):                                                                                              #Traverse mat.
            if mat[i][j]:
                continue
            q.append((i, j))                                                                                                                  #Append current cell to queue.
            distance[i][j] = 0                                                                                                                #Set its distance to 0.
        while q:                                                                                                                              #BFS.
            newq = []                                                                                                                         #Initialize new queue.
            for i, j in q:                                                                                                                    #For each cell in q, traverse the 4 neighbors.
                for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                    if 0 <= x < m and 0 <= y < n and mat[x][y] and distance[x][y] > distance[i][j]:                                           #If neighbor is valid, is 1 and has larger distance, set it to be distance of current cell plus 1 and append neightbor to newq.
                        distance[x][y] = distance[i][j] + 1
                        newq.append((x, y))
            q = newq                                                                                                                          #Replace q with newq.
        return distance                                                                                                                       #Return distance.
