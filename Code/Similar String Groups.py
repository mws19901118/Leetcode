class UnionFind:                                                                                                        #Union-Find class.
    def __init__(self, x: int):
        self.parent = None
        self.label = x

    def find(self) -> 'UnionFind':
        if not self.parent:
            return self
        self.parent = self.parent.find()
        return self.parent

    def union(self, uf: 'UnionFind') -> None:
        if not self.find().label == uf.find().label:
            self.find().parent = uf.find()

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def isSimilar(s1: str, s2: str):                                                                                #Determine if 2 strings are similar.
            unMatches = [(x, y) for x, y in zip(s1, s2) if x != y]                                                      #Find all unmatched pairs.
            return not unMatches or (len(unMatches) == 2 and (unMatches[1][1], unMatches[1][0]))                        #There should be either no unmatched pairs or only 2 unmatched pairs and the second one is the reverse of first one.

        ufs = [UnionFind(i) for i in range(len(strs))]                                                                  #Initialize a Union-Find for each string.
        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):                                                                           #Traverse each string pair.
                if isSimilar(strs[i], strs[j]):                                                                         #If they are similar, union the 2 Union-Finds.
                    ufs[i].union(ufs[j])
        
        return len(set([uf.find().label for uf in ufs]))                                                                #Return the size of Union-Find parent label.
