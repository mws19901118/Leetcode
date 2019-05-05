class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:                                                 #If either demension of matrix is 0, return empty list.
            return []
        m, n = len(matrix), len(matrix[0])
        pacific = set()                                                                 #Use a set to records the cells where water can flow to pacific.
        q = set([(0, i) for i in range(n)]) | set([(j, 0) for j in range(m)])           #The initail cells for pacific(left and top edges).
        while q:                                                                        #BFS.
            nextq = set()                                                               #Coordinates for next level of BFS.
            pacific |= q                                                                #Update visited, aka pacific.
            for p in q:
                for d in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                    nextp = (p[0] + d[0], p[1] + d[1])
                    if 0 <= nextp[0] < m and 0 <= nextp[1] < n and nextp not in pacific and matrix[nextp[0]][nextp[1]] >= matrix[p[0]][p[1]]:
                        nextq.add(nextp)                                                #For each adjacet cell of current cell, add the valid unvisited cell whose height is not smaller than current set to nextq.
            q = nextq                                                                   #Replace q with nextq.
        
        atlantic = set()                                                                #Use a set to records the cells where water can flow to pacific.
        q = set([(m - 1, i) for i in range(n)]) | set([(j, n - 1) for j in range(m)])   #The initail cells for pacific(right and bottom edges).
        while q:                                                                        #BFS.
            nextq = set()                                                               #Coordinates for next level of BFS.
            atlantic |= q                                                               #Update visited, aka atlantic.
            for p in q:
                for d in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                    nextp = (p[0] + d[0], p[1] + d[1])
                    if 0 <= nextp[0] < m and 0 <= nextp[1] < n and nextp not in atlantic and matrix[nextp[0]][nextp[1]] >= matrix[p[0]][p[1]]:
                        nextq.add(nextp)                                                #For each adjacet cell of current cell, add the valid unvisited cell whose height is not smaller than current set to nextq.
            q = nextq
        
        return list(pacific & atlantic)                                                 #Return the list of intersect of pacific and atlantic.
