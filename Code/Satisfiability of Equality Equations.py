class UnionFind:                                                                                                      #Union find class.
    def __init__(self):
        self.parent = self
    
    def find(self):
        if self.parent == self:
            return self
        self.parent = self.parent.find()
        return self.parent

    def union(self, x) -> None:
        self.find().parent = x.find()

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        unionFinds = defaultdict(lambda: UnionFind())                                                                 #Use a defaultdict to store union finds for each letter.
        for e in equations:                                                                                           #Traverse each equal equations.
            if e[1:3] == "==":
                unionFinds[e[0]].union(unionFinds[e[-1]])                                                             #Build the relations between union finds.
        return all(unionFinds[e[0]].find() != unionFinds[e[-1]].find() for e in equations if e[1:3] == "!=")          #For each unequal union finds, their parent shouldn't be same; otherwise, return false.
