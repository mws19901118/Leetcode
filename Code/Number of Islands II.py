class UnionFind:                                                                                                            #Union-Find class.
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
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        count, result, ufs = 0, [], {}                                                                                      #Initialize count, result and Union-Finds.
        for i, j in positions:                                                                                              #Traverse positions.
            if (i, j) not in ufs:                                                                                           #If (i, j) is not in ufs, it's a new island.
                ufs[(i, j)] = UnionFind((i, j))                                                                             #Create a new Union-Find for (i, j).
                count += 1                                                                                                  #Increase count.
                for x, y in [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]:                                               #Traverse all neighbors.
                    if (x, y) in ufs and not ufs[(i, j)].union(ufs[(x, y)]):                                                #If neighbor is valid and is island and can be unioned with current island, decrease count.
                        count -= 1
            result.append(count)                                                                                            #Append count to result.
        return result
