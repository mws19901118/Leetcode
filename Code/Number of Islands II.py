class UnionFind:                                                                                                            #Union find.
    def __init__(self, position: (int, int)) -> None:
        self.position = position
        self.parent = None
    
    def find(self) -> 'UnionFind':                                                                                          #Find the parent of current node. 
        if not self.parent:
            return self
        self.parent = self.parent.find()
        return self.parent

    def union(self, uf: 'UnionFind') -> bool:                                                                               #Union current node with another node, and return whether the union is needed.
        if self.find().position != uf.find().position:
            self.find().parent = uf.find()
            return True
        return False
        
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        count, result, ufs = 0, [], {}                                                                                      #Initialize count, result and union finds.
        for i, j in positions:                                                                                              #Traverse positions.
            if (i, j) not in ufs:                                                                                           #If (i, j) is not in ufs, it's a new island.
                ufs[(i, j)] = UnionFind((i, j))                                                                             #Create a new UnionFind for (i, j).
                count += 1                                                                                                  #Increase count.
                for x, y in [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]:                                               #Traverse all neighbors.
                    if 0 <= x < m and 0 <= y < n and (x, y) in ufs and ufs[(i, j)].union(ufs[(x, y)]):                      #If neighbor is valid and is island and can be unioned with current island, decrease count.
                        count -= 1
            result.append(count)                                                                                            #Append count to result.
        return result
