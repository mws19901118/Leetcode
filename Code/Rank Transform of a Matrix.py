class UnionFind:                                                                        #Union-Finds manager.
    def __init__(self):
        self.parent = {}                                                                #Use a dict to store the parent of each number.
        
    def find(self, u):                                                                  #Find the parent of u.
        if u != self.parent[u]:                                                         #If u is not in top level, find the parent of parent of u and update the parent of u.
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]                                                           #Return the parent of u.
    
    def union(self, u, v):                                                              #Union 2 numbers u and v.
        self.parent.setdefault(u, u)                                                    #Add u to union find if u is not added yet.
        self.parent.setdefault(v, v)                                                    #Add v to union find if v is not added yet.
        pu, pv = self.find(u), self.find(v)                                             #Find the parent of u and parent of v.
        if pu != pv:                                                                    #If pu != pv, point parent of pu to pv.
            self.parent[pu] = pv
            
    def getGroups(self):                                                                #Group Union-Finds with same parent.
        groups = defaultdict(list)                                                      #Initialize groups.
        for i in self.parent.keys():                                                    #Traverse Union-Finds and add each Union-Find to corresponding group by its parent. 
            groups[self.find(i)].append(i)
        return groups                                                                   #Return groups.

class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])                                              #Get dimensions.
        cells = defaultdict(list)                                                       #Store the coordinates of each cell by value.
        for i, j in product(range(m), range(n)):                                        #Traverse matrix to fill cells.
            cells[matrix[i][j]].append([i, j])
        rank = [0] * (m + n)                                                            #Initialize largest rank of the row or column so far.
        for x in sorted(cells):                                                         #Traverse the sorted keys of cells.
            uf = UnionFind()                                                            #Initalize Union-Finds manager for all cells with value x.
            for r, c in cells[a]:                                                       #Traverse all cells with value x.
                uf.union(r, c + m)                                                      #Union row r with column c (c + m to separate with r).
            for group in uf.getGroups().values():                                       #Traverse all groups of cells with value x.
                maxRank = max(rank[i] for i in group)                                   #Get max rank of all rows and columns which has cell from current group.
                for i in group:
                    rank[i] = maxRank + 1                                               #Update all rows and columns in the same groups to new rank(maxRank + 1).
            for r, c in cells[x]:
                matrix[r][c] = rank[r]                                                  #Update matrix[r][c] to be its rank(rank[r] or rank[c + m])
        return matrix                                                                   #Return matrix.
