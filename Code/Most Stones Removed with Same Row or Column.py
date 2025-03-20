class UnionFind:                                                                     #Union-Find class.
    def __init__(self, x: int):
        self.parent = None
        self.label = x

    def find(self) -> 'UnionFind':
        if not self.parent:
            return self
        self.parent = self.parent.find()
        return self.parent

    def union(self, uf: 'UnionFind') -> bool:
        if self.find().label == uf.find().label:
            return True
        self.find().parent = uf.find()
        return False

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rows, columns = {}, {}                                                      #Store the index of first stone in each row and column.
        ufs = [UnionFind((x, y)) for x, y in stones]                                #Initialize a Union-Find for each stone.
        for i, (x, y) in enumerate(stones):                                         #Traverse stones.
            if x not in rows:                                                       #If x not in rows, set rows[x] to i.
                rows[x] = i
            else:                                                                   #Otherwise, union ufs[i] with ufs[rows[x]].
                ufs[i].union(ufs[rows[x]])
            if y not in columns:                                                    #If x not in columns, set columns[y] to i.
                columns[y] = i
            else:                                                                   #Otherwise, union ufs[i] with ufs[columns[x]].
                ufs[i].union(ufs[columns[y]])
        return len(stones) - len(set(uf.find().label for uf in ufs))                #Group ufs by the label of their parents. We can leave one stone for each group and remove the rest.
