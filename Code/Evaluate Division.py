class Solution:
    def DFS(self, start: str, visited: set, stack: List[tuple], edges: defaultdict, ratios: dict):                #DFS.
        if not stack:                                                                                             #If stack is empty, return.
            return
        node, ratio = stack.pop()                                                                                 #Pop the latest ratio node and ratio value.
        visited.add(node)                                                                                         #Add node to visited.
        ratios[node] = (start, ratio)                                                                             #Set it's ratio to start node in ratios.
        for x, r in edges[node]:
            if x not in visited:                                                                                  #For each unvisited adjacent node x, push the node and node's ratio to start node to stack as tuple.
                stack.append((x, ratio * r))
                self.DFS(start, visited, stack, edges, ratios)
                
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        edges = defaultdict(list)
        for e, v in zip(equations, values):                                                                       #Create graph.
            edges[e[1]].append((e[0], v))                                                                         #For equation a / b = v, the weight of edge a to b is 1 / v while the weight of edge b to a is v.
            edges[e[0]].append((e[1], 1 / v))
        ratios = {}                                                                                               #Keep the ratios of each variable to a reference variable connected to it in graph.
        visited = set()                                                                                           #Store all visited nodes.
        for x in edges:
            if x not in visited:
                self.DFS(x, visited, [(x, 1)], edges, ratios)                                                     #For each unvisited node x, do DFS with initial stack is (x, 1), means initially x's ratio to itself is 1.
        result = []                                                                                               #Store result.
        for q0, q1 in queries:
            if q0 not in ratios or q1 not in ratios or ratios[q0][0] != ratios[q1][0]:                            #For each query a / b, if either variable is not in ratios or the reference of a and b in ratios is not the same, add -1.00000 to result.
                result.append(-1.00000)
            else:                                                                                                 #Otherwise, add the ratio of a's ratio and b's ratio to result.
                result.append(ratios[q0][1] / ratios[q1][1])
        return result
                
            
