class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)                                                       #Get n.
        adjacentList = [[] for _ in range(n)]                                 #Build adjacent list.
        for x, y in edges:
            adjacentList[x].append(y)
        cache = {}                                                            #Cache intermedia result.

        def DFS(node: int, visited: Set[int]) -> Counter:                     #DFS.
            if node in cache:                                                 #If node is in cache, return cache[node].
                return cache[node]
            count = Counter()                                                 #Initialize a counter to store the max count of each color starting from current node.
            for x in adjacentList[node]:                                      #Traverse each neighbor of node.
                if x in visited:                                              #If x is visited, return none because there is a cycle.
                    return None
                visited.add(x)                                                #Add x to visited.
                next_count = DFS(x, visited)                                  #Get the counter from x.
                if next_count == None:                                        #If it is none, there is a cycle, return none as well.
                    return None
                for y in next_count:                                          #For each color in next_count, update its max value in count.
                    count[y] = max(count[y], next_count[y])
                visited.remove(x)                                             #Remove x from visited.
            count[colors[node]] += 1                                          #Increase the count of current node color.
            cache[node] = count                                               #Set count in cache for current node.
            return count                                                      #Return count.

        result = -1                                                           #Initialize result.
        for x in range(n):                                                    #DFS from each node.
            count = DFS(x, set([x]))
            if not count:                                                     #If there is a cycle, return -1.
                return -1
            result = max(result, max(count.values()))                         #Update result if the longest color from current DFS is longer.
        return result                                                         #Return result.
