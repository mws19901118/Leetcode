class UnionFind:                                                                                                  #Union Find class.
    def __init__(self, id: int):
        self.id = id
        self.parent = None

    def find(self) -> 'UnionFind':
        if not self.parent:
            return self
        self.parent = self.parent.find()
        return self.parent

    def union(self, uf: 'UnionFind') -> None:
        if self.find().id != uf.find().id:
            self.find().parent = uf.find()

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        ufs = {i:UnionFind(i) for i in range(1, c + 1)}                                                          #Create a union find for each station.
        for x, y in connections:                                                                                 #Union based on connections.
            ufs[x].union(ufs[y])
        grid = defaultdict(SortedSet)                                                                            #Store the online station ids of each power grid in ascending order based on the grid id(parent id of current union).
        for uf in ufs.values():                                                                                  #Add the station ids to the grid.
            grid[uf.find().id].add(uf.id)
        offline = set()                                                                                          #Store offline stations ids.
        result = []
        for label, x in queries:                                                                                 #Traverse queries.
            if label == 2:                                                                                       #If it is offline operation, add the station id to offline and discard the id from its grid.
                offline.add(x)
                grid[ufs[x].find().id].discard(x)
            elif x not in offline:                                                                               #If current station is not offline, append id to result.
                result.append(x)
            elif not grid[ufs[x].find().id]:                                                                     #If all the stations in grid are offline, append -1 to result.
                result.append(-1)
            else:                                                                                                #Otherwise, append the smallest station id in grid to result.
                result.append(grid[ufs[x].find().id][0])
        return result
