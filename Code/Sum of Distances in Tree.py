class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adjacentList = [[] for _ in range(n)]                                                                                            #Build adjacent list.
        for x, y in edges:
            adjacentList[x].append(y)
            adjacentList[y].append(x)
        
        result, count, distance = [0] * n, [0] * n, [0] * n                                                                              #Initialize result, also node count for each subtree and total distance of all nodes in subtree to current root for each subtree.
        def findCountAndDistanceInSubtree(curr: int, prev: int):                                                                         #Populate count and distance.
            count[curr], distance[curr] = 1, 0                                                                                           #Initialize count[curr] and distance[curr].
            for x in adjacentList[curr]:                                                                                                 #Traverse adjacentList[curr].
                if x == prev:                                                                                                            #If x is prev, skip because it's parent of curr.
                    continue
                findCountAndDistanceInSubtree(x, curr)                                                                                   #Recursively populate count and distance for the subtree whose root is x.
                count[curr] += count[x]                                                                                                  #Add count[x] to count[curr].
                distance[curr] += distance[x] + count[x]                                                                                 #Add distance[x] + count[x] to distance[curr].

        def updateResult(curr: int, prev: int, countFromAbove: int, distanceFromAbove: int):                                             #Update result with count and distance passed from parent and siblings.
            result[curr] = distance[curr] + distanceFromAbove                                                                            #Sum of distance to curr is the sum of distance passed from parent and siblings plus total distance of all nodes in subtree to current root.
            for x in adjacentList[curr]:                                                                                                 #Traverse adjacentList[curr].
                if x == prev:                                                                                                            #If x is prev, skip because it's parent of curr.
                    continue
                nextCountFromAbove = countFromAbove + count[curr] - count[x]                                                             #Count to be passed to x is countFromAbove plus count of nodes in the subtree whose root is curr but not in the subtree whose root is x.
                nextDistanceFromAbove = distanceFromAbove + nextCountFromAbove + distance[curr] - distance[x] - count[x]                 #Distance to be passed to x is distanceFromAbove + (distance[curr] - distance[x] - count[x])(distance in subtree whose root is curr except those from x), then plus nextCountFromAbove.
                updateResult(x, curr, nextCountFromAbove, nextDistanceFromAbove)                                                         #Recursively update result with updated count from above and distance from above.
        
        findCountAndDistanceInSubtree(0, -1)                                                                                             #Populate count and distance from node 0.
        updateResult(0, -1, 0, 0)                                                                                                        #Update result from node 0, with no count and distance from above.
        return result
