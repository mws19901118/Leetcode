class Solution:
    def DFS(self, graph: defaultdict[List], color: dict, index: int, currentColor: int) -> bool:
        if index in color:                                                                      #If current person is already colored, check if its color is the same as current color.
            return color[index] == currentColor
        color[index] = currentColor                                                             #Color current person.
        return all(self.DFS(graph, color, i, 1 ^ currentColor) for i in graph[index])           #Color all neighbor with opposite color.
    
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)                                                               #Construct a graph.
        for x, y in dislikes:
            graph[x].append(y)
            graph[y].append(x)
        color = {}
        return all(self.DFS(graph, color, i, 0) for i in range(n) if i not in color)            #For each connected component, we can check whether it is bipartite by just trying to coloring it with two colors.
