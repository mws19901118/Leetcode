class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def bfs(start: int):                                                                #BFS.
            curr, length, visited, distance = start, 0, set(), [100001] * len(edges)        #Initializee cursor, current length, visited nodes and the distance to each node.
            while curr != -1 and curr not in visited:                                       #Traverse until curr is -1 or is visited.
                visited.add(curr)                                                           #Mark curr as visited.
                distance[curr] = length                                                     #Set distance[curr] to length.
                curr = edges[curr]                                                          #Move curr to edges[curr].
                length += 1                                                                 #Increase length.
            return distance                                                                 #Return distance.
        
        distance1, distance2 = bfs(node1), bfs(node2)                                       #BFS from node1 and node2 respectively.
        index, minMaxDistance = -1, 100001                                                  #Initialize index and minimum of max distances between nodes.
        for i in range(len(edges)):                                                         #Traverse 2 distances simultaneously.
            if minMaxDistance > max(distance1[i], distance2[i]):                            #If the max distance is greater than minMaxDistance, update minMaxDistance and index.
                minMaxDistance = max(distance1[i], distance2[i])
                index = i
        return index                                                                        #Return index.
