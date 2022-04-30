class Solution:
    def DFS(self, start: str, stack: List[tuple], edges: defaultdict, ratios: dict):                                                                            #DFS.
        if not stack:                                                                                                                                           #If stack is empty, return.
            return
        node, ratio = stack.pop()                                                                                                                               #Pop the latest ratio node and ratio value.
        ratios[node] = (start, ratio)                                                                                                                           #Set it's ratio to start node in ratios.
        for x, r in edges[node]:
            if x not in ratios:                                                                                                                                 #For each unvisited adjacent node x, push the node and node's ratio to start node to stack as tuple.
                stack.append((x, ratio * r))
                self.DFS(start, stack, edges, ratios)
                
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        edges = defaultdict(list)
        for e, v in zip(equations, values):                                                                                                                     #Build graph.
            edges[e[1]].append((e[0], v))                                                                                                                       #For equation a / b = v, the weight of edge a to b is 1 / v while the weight of edge b to a is v.
            edges[e[0]].append((e[1], 1 / v))
        ratios = {}                                                                                                                                             #Keep the ratios of each variable to a reference variable connected to it in graph.
        for x in edges:
            if x not in ratios:
                self.DFS(x, [(x, 1)], edges, ratios)                                                                                                            #For each unvisited node x, do DFS with initial stack is (x, 1), means initially x's ratio to itself is 1.
        
        return [-1.00000 if q0 not in ratios or q1 not in ratios or ratios[q0][0] != ratios[q1][0] else ratios[q0][1] / ratios[q1][1] for q0, q1 in queries]    #For each query q0 / q1, if either variable is not in ratios or the reference of q0 and q1 in ratios is not the same, add -1.00000 to result; otherwise, add the ratio of q0's ratio to q1's ratio to result.

                
            
class UnionFind:                                                                                                                                                                                        #Union find.
    def __init__(self, name: str, ratio: float):
        self.ratio = ratio                                                                                                                                                                              #Store the ratio of current variable to parent variable.
        self.name = name                                                                                                                                                                                #Store current variable name.
        self.parent = self                                                                                                                                                                              #Initially, point parent to self.
        
    def union(self, uf, ratio) -> None:                                                                                                                                                                 #Union current variable with target variable with ratio.
        x = self.find()                                                                                                                                                                                 #Find the parent of current variable.
        if x.name != uf.find().name:                                                                                                                                                                    #If name of parent is same with name of parent of target variable, they are already unioned.
            x.ratio = ratio / self.ratio                                                                                                                                                                #Update the ratio of parent to be the ratio to target vairable.
            x.parent = uf                                                                                                                                                                               #Point the parent of parent to target variable.
        
    def find(self):                                                                                                                                                                                     #Find the parent of a variable.
        if self.parent == self:                                                                                                                                                                         #If parent is self, return self directly.
            return self
        x = self.parent                                                                                                                                                                                 #Find current parent.
        self.parent = self.parent.find()                                                                                                                                                                #Set parent to the parent of current parent to compress path.
        self.ratio *= x.ratio                                                                                                                                                                           #Update ratio to be the ratio to parent of parent.
        return self.parent                                                                                                                                                                              #Return new parent.
    
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        unionFinds = {}                                                                                                                                                                                 #Instantiate UnionFind dictionary by variable name.
        for (x, y), v in zip(equations, values):                                                                                                                                                        #Populate dictionary for each equation.
            if x not in unionFinds:                                                                                                                                                                     #If x not in dictionary, instantiate a UnionFind for x at unionFinds[x].
                unionFinds[x] = UnionFind(x, 1.0)
            if y not in unionFinds:                                                                                                                                                                     #If y not in dictionary, instantiate a UnionFind for y at unionFinds[y].
                unionFinds[y] = UnionFind(y, 1.0)
            unionFinds[x].union(unionFinds[y], v)                                                                                                                                                       #Union unionFinds[x] with unionFinds[y] with ratio v.
            
        return [unionFinds[x].ratio / unionFinds[y].ratio if x in unionFinds and y in unionFinds and unionFinds[x].find().name == unionFinds[y].find().name else -1.00000 for x, y in queries]          #For each query x / y, if either variable is not in unionFinds or the parent name of x and y is not the same, add -1.00000 to result; otherwise, add the ratio of parent of x to ratio of parent of y to result.
