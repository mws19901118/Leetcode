class UnionFind:                                                                          #Union-Find class.
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
            return False
        self.find().parent = uf.find()
        return True

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        ufs = [UnionFind(i) for i in range(n)]                                            #Instentiate a Union-Find for each person.
        for t, x, y in sorted(logs):                                                      #Sort logs by timestamp in asending order and traverse.
            if ufs[x].union(ufs[y]):                                                      #If ufs[x] and ufs[y] needs union, they become friends at current time, decrease n by 1.
                n -= 1
            if n == 1:                                                                    #When n == 1, all people have become friends, return t.
                return t
        return -1                                                                         #Return -1 if not all people have become friends after traverse.
