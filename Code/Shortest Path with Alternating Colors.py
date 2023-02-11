class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        adjacentListRed, adjacentListBlue = collections.defaultdict(list), collections.defaultdict(list)      #Build adjacent list for red edges and blue edges respectively.
        for x, y in redEdges:
            adjacentListRed[x].append(y)
        for x, y in blueEdges:
            adjacentListBlue[x].append(y)
        visitedRed, visitedBlue = set([0]), set([0])                                                          #Initialize visited nodes from red edges and blue edges respectively.
        result = [-1] * n                                                                                     #Initialize result.
        q = [(0, None)]                                                                                       #Initialize queue starting from node 0, which is considered from both red and blue edges.
        count = 0                                                                                             #Initialize count.
        while q:                                                                                              #BFS.
            newq = []                                                                                         #Initialize new queue.
            for x, fromRed in q:                                                                              #Traverse queue.
                if result[x] == -1:                                                                           #If current node is not reached, set the length to count.
                    result[x] = count
                if fromRed is None or fromRed:                                                                #If current node is reached from red edge, continue BFS on red adjacent list.
                    for y in adjacentListBlue[x]:
                        if y not in visitedBlue:
                            visitedBlue.add(y)
                            newq.append((y, False))
                if fromRed is None or not fromRed:                                                            #If current node is reached from blue edge, continue BFS on blue adjacent list.
                    for y in adjacentListRed[x]:
                        if y not in visitedRed:
                            visitedRed.add(y)
                            newq.append((y, True))
            q = newq                                                                                          #Replace queue with new queue.
            count += 1                                                                                        #Increase count.
        return result
