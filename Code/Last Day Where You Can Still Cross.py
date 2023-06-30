class UnionFind:                                                                              #Union find.
    def __init__(self, leftBound: int, rightBound: int):                                      #Instentiate union find with columnwise left bound and right bound.
        self.leftBound = leftBound
        self.rightBound = rightBound
        self.parent = None

    def find(self) -> 'UnionFind':                                                            #Find the parent of current union find.
        if not self.parent:
            return self
        self.parent = self.parent.find()
        return self.parent

    def union(self, uf: 'UnionFind') -> None:                                                 #Union current union find with uf.
        if not self.find() == uf.find():                                                      #If the parent of current union find and the parent of uf is same, then they are already unioned.
            self.find().parent = uf.find()
            self.find().leftBound = min(self.find().leftBound, self.leftBound)                #Update the left bound of new parent.
            self.find().rightBound = max(self.find().rightBound, self.rightBound)             #Update the right bound of new parent.

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        days = 0                                                                              #Initialize days.
        ufDict = {}                                                                           #Store union finds based on the coordinate.
        for x, y in cells:                                                                    #Traverse cells.
            ufDict[(x, y)] = UnionFind(y, y)                                                  #Create a union find for current water cell.
            for u, v in product([x - 1, x, x + 1], [y - 1, y, y + 1]):                        #Traverse all neighbors in 8 directions.
                if (u, v) == (x, y) or (u, v) not in ufDict:                                  #If it's same as current cell or is not seen yet in ufDicts, skip.
                    continue
                uf = ufDict[(x, y)].find()                                                    #Find the parent of current union find.
                uf.union(ufDict[u, v])                                                        #Union it with neighbor.
                if uf.find().leftBound == 1 and uf.find().rightBound == col:                  #After union, If the left bound of parent is 1 and right bound of parent is col, this union find set can block all culumns, so return days.
                    return days
            days += 1                                                                         #Increase days.
        return days                                                                           #Return days if no blocking at the end. 

