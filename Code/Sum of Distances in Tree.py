class Solution:
    def sumDistanceAndNode(self, n: int, p: int, adjacentList: List[List[int]], distanceAndNodeSum: List[tuple]) -> None:
        distanceSum, nodeSum = 0, 0                                                                                                                                               #Initialize total distance to current root and node count.
        for x in adjacentList[n]:                                                                                                                                                 #Traverse adjacentList[n].
            if x == p:                                                                                                                                                            #If x is the previous node of n, skip.
                continue
            self.sumDistanceAndNode(x, n, adjacentList, distanceAndNodeSum)                                                                                                       #Populate distanceAndNodeSum for x.
            distanceSum += distanceAndNodeSum[x][0]                                                                                                                               #Increate distanceSum by distanceAndNodeSum[0].
            nodeSum += distanceAndNodeSum[x][1]                                                                                                                                   #Increate nodeSum by 1.
        distanceSum += nodeSum                                                                                                                                                    #Now distanceSum is the sum of distances in its lower level, all nodes are 1 edge away from connecting to n. So, add nodeSum to distanceSum.
        nodeSum += 1                                                                                                                                                              #Increase 1 to nodeSum because of n itself.
        distanceAndNodeSum[n] = (distanceSum, nodeSum)                                                                                                                            #Update distanceAndNodeSum[n].

    def dfs(self, n: int, distanceFromParent: int, nodesFromParent, result: List[int], adjacentList: List[List[int]], distanceAndNodeSum: List[tuple]) -> None:
        distanceSumFromLowerLevel =  sum(distanceAndNodeSum[x][0] + distanceAndNodeSum[x][1] for x in adjacentList[n] if result[x] == 0)                                          #Traverse adjacentList[n] and skip the one whose result is already set(meaning that node is traversed so it's the parent of n), and sum up total distances and node count to get the distances sum from lower levels to n.
        result[n] = distanceFromParent + distanceSumFromLowerLevel                                                                                                                #Overall, result[n] equals the distance from lower levels and distances carried over from parent.
        for x in adjacentList[n]:                                                                                                                                                 #Traverse adjacentList[n]. 
            if result[x] != 0:                                                                                                                                                    #If result[x] is already set, x is traversed so it's the parent of n and we need to skip x.
                continue
            carryOverNodes = nodesFromParent + distanceAndNodeSum[n][1] - distanceAndNodeSum[x][1]                                                                                #Calculate the carry over nodes count, which equals nodesFromParent plus all nodes under n except nodes under x
            carryOverDistances = result[n] - distanceAndNodeSum[x][0] - distanceAndNodeSum[x][1] + carryOverNodes                                                                 #Calculate the carry over to x. Extract distances from x to n. Then add carryOverNodes, because they are 1 edge away from connecting to x.
            self.dfs(x, carryOverDistances, carryOverNodes, result, adjacentList, distanceAndNodeSum)                                                                             #Keep dfs at x.
    
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adjacentList = [[] for _ in range(n)]                                                                                                                                     #Initialize adjacent list.
        for a, b in edges:                                                                                                                                                        #Build adjacent list.
            adjacentList[a].append(b)
            adjacentList[b].append(a)
        distanceAndNodeSum = [None] * n                                                                                                                                           #Initialize the total distance to current root and node count of subtree at each node. 
        result = [0] * n                                                                                                                                                          #Initialize result of each node.
        self.sumDistanceAndNode(0, None, adjacentList, distanceAndNodeSum)                                                                                                        #Populate distanceAndNodeSum for each node, starting from node 0.
        self.dfs(0, 0, 0, result, adjacentList, distanceAndNodeSum)                                                                                                               #Populate result for each node, starting from node 0.
        return result                                                                                                                                                             #Return result.
