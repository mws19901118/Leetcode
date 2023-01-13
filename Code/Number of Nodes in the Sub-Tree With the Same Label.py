class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adjacentList = collections.defaultdict(list)                                    #Build the adjacent list.
        for x, y in edges:
            adjacentList[x].append(y)
            adjacentList[y].append(x)
        result = [0] * n                                                                #Initialze the result to be 0 for all nodes.

        def DFS(curr: int, prev: int) -> collections.Counter:
            count = collections.Counter()                                               #Initialize a counter.
            count[labels[curr]] = 1                                                     #The node count of current label is 1.
            for x in adjacentList[curr]:                                                #Traverse neighbors.
                if x == prev:                                                           #If x is same as prev, it's visited, so skip.
                    continue
                for k, v in DFS(x, curr).items():                                       #Traverse the DFS result from neighbor.
                    count[k] += v                                                       #Add all count of node to current counter.
            result[curr] = count[labels[curr]]                                          #Set the result for current node.
            return count                                                                #Return counter.

        DFS(0, -1)                                                                      #DFS from node 0.
        return result
