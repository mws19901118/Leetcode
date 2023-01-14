class UnionFind:                                                                          #Union find.
    def __init__(self, x: str) -> None:
        self.parent = None
        self.label = x

    def find(self) -> 'UnionFind':
        if not self.parent:
            return self
        self.parent = self.parent.find()
        return self.parent

    def union(self, uf: 'UnionFind') -> None:                                             #When union, the lexicographically smaller label always win.
        if self.find().label > uf.find().label:
            self.find().parent = uf.find()
        elif self.find().label < uf.find().label:
            uf.find().parent = self.find()
    
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        letters = 'abcdefghijklmnopqrstuvwxyz'                                            #Initialize all letters.
        ufs = {x: UnionFind(x) for x in letters}                                          #Instentiate a UnionFind for each letter.
        for x, y in zip(s1, s2):                                                          #Traverse s1 and s2 simultaneously.
            ufs[x].union(ufs[y])                                                          #Union the 2 letters.
        mapping = {x: ufs[x].find().label for x in letters}                               #Build the mapping of each letter to its parent.
        return "".join([mapping[x] for x in baseStr])                                     #Map each letter in baseStr and join to get the lexicographically smallest equivalent string.
