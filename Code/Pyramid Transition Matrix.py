class Solution:
    def DFS(self, graph, lastLevel, currentLevel):                              #DFS based on last level and current level.
        if len(lastLevel) == 1:                                                 #If the length of last level is 1, it already build the pyramid all the way to top, return true.
            return True
        for b in graph[lastLevel[len(currentLevel):len(currentLevel) + 2]]:     #Try every allowed block for current position.
            t = currentLevel + b
            if len(t) == len(lastLevel) - 1:                                    #If this is the last position of current level, DFS starts with current level as last level and an empty current level.
                if self.DFS(graph, t, ""):
                    return True
            else:
                if self.DFS(graph, lastLevel, t):                               #DFS next positon in current level.
                    return True                                                 #If can build pyramid, return true immediately to prune the search tree.
        return False                                                            #Otherwise, return false.
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        graph = collections.defaultdict(list)
        for t in allowed:                                                       #Construct the graph for each allowed triple.
            graph[t[0:2]].append(t[2])                                          #The graph is directed from the combination of left block and right block to top block.
        
        return self.DFS(graph, bottom, "")                                      #DFS.
