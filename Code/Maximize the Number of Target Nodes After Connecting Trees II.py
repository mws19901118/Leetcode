class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def countTargetForEachNode(edges: List[List[int]], isEven: bool) -> List[int]:    #Count target for each node given edges and if the target requires even edges.
            adjacentList = defaultdict(list)                                              #Build adjacent list.
            for x, y in edges:
                adjacentList[x].append(y)
                adjacentList[y].append(x)
            count = Counter()                                                             #Initialize counter.
            
            def dfs_calculate(curr: int, prev: int) -> None:                              #DFS to calculate the odd distance nodes and even distance nodes of curr in the subtree whose root is curr.
                count[(curr, False)], count[(curr, True)] = 0, 1                          #The curr node is an even distance node to itself.
                for x in adjacentList[curr]:                                              #Traverse the neighbors of x.
                    if x != prev:                                                         #Skip if x is prev.
                        dfs_calculate(x, curr)                                            #Keep DFS from x.
                        count[(curr, False)] += count[(x, True)]                          #Add the even distance nodes of x to the odd distance nodes of curr.
                        count[(curr, True)] += count[(x, False)]                          #Add the odd distance nodes of x to the even distance nodes of curr.
            
            def dfs_propagate(curr: int, prev: int) -> None:                              #DFS to propagate the odd distance nodes and even distance nodes of curr to its children.
                if prev is not None:                                                      #If prev is not none, update the odd distance nodes of curr to be the even distance nodes of prev and update the even distance nodes of curr to the odd distance nodes of prev.
                    count[(curr, False)] = count[(prev, True)]                            #Because in the tree, nodes with same depth parity are equivalent in terms of odd distance nodes and even distance nodes.
                    count[(curr, True)] = count[(prev, False)]
                for x in adjacentList[curr]:                                              #Traverse the neighbors of x.
                    if x != prev:                                                         #Skip if x is prev.
                        dfs_propagate(x, curr)                                            #Keep DFS from x.
            
            dfs_calculate(0, None)                                                        #Start calulation DFS from node 0 as root.
            dfs_propagate(0, None)                                                        #Start propagation DFS from node 0 as root.
            return [count[(i, isEven)] for i in range(len(edges) + 1)]                    #Return the target of each node based on the requirement of odd or even edges.
        
        count1 = countTargetForEachNode(edges1, True)                                     #Count target for each node in tree1 with even edges.
        count2 = countTargetForEachNode(edges2, False)                                    #Count target for each node in tree2 with odd edges.
        maxCount2 = max(count2)                                                           #Since we can connect to any node in tree2, we just connect to the node with max target.
        return [count1[i] + maxCount2 for i in range(len(edges1) + 1)]                    #Return count1[i] + maxCount2 for each node in tree1.
