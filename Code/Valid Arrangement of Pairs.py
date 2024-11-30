class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        adjacentList, inDegree, outDegree = defaultdict(list), defaultdict(int), defaultdict(int)         #Initialize adjacent list, indegree and outdegree.
        for x, y in pairs:                                                                                #Traverse pairs.
            adjacentList[x].append(y)                                                                     #Build adjacent list to add an edge from x to y.
            outDegree[x] += 1                                                                             #Increase the outdegree of x.
            inDegree[y] += 1                                                                              #Increase the indegree of y.
        result = []                                                                                       #Initialize result.
      
        def dfs(node: int):                                                                               #Traverse graph using DFS.
            while adjacentList[node]:                                                                     #While there are neighbors, pop neighbor from adjacent list of current node and keep traversing at neighbor.
                nextNode = adjacentList[node].pop()
                dfs(nextNode)
            result.append(node)                                                                           #Append node to result.

        candidates = [x for x in outDegree if outDegree[x] == inDegree[x] + 1]                            #Find the candidates to start traverse; their outdegree should be indegree plus 1.
        startNode = pairs[0][0] if not candidates else candidates[0]                                      #If no such candidates, either node is okay, so use the first one; otherwise use the node in candidates.
        dfs(startNode)                                                                                    #DFS.
        result.reverse()                                                                                  #Reverse result since the order of appending to result is the later nodes inserted first.
        return [[result[i - 1], result[i]] for i in range(1, len(result))]                                #Restore it to pairs and return.
