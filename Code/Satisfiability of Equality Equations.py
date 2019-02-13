class UnionFind:                                                      #Union Find.
    def __init__(self, value):
        self.parent = self
        self.value = value
    
    def union(self, a):
        self.find().parent = a.find()
    
    def find(self):
        p = self.parent
        while p != p.parent:
            p = p.parent
        return p
    
class Solution:
    def equationsPossible(self, equations: 'List[str]') -> 'bool':
        nonEqualPairs = []
        d = {}                                                        #Use dict to store union find.
        for e in equations:
            if e[0] not in d:                                         #Initialize union find.
                d[e[0]] = UnionFind(e[0])
            if e[3] not in d:
                d[e[3]] = UnionFind(e[3])
            if e[1:3] == "==":                                        #If the equaltion is "equal", union the 2 variables.
                d[e[0]].union(d[e[3]])
            else:                                                     #If the equaltion is "not equal", store the pair of variables in a list.
                nonEqualPairs.append((e[0], e[3]))
        
        for p in nonEqualPairs:                                       #For each pair of vairables that are not equal, if their union find have the same parent, then the equaltion list can't be satisfied.
            if d[p[0]].find() == d[p[1]].find():
                return False
        return True
