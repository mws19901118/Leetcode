class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        distance1, distance2 = [100001] * len(edges), [100001] * len(edges)           #Initialize the distance of each node to node1 and node2.
        def BFS(start: int, distance: List[int]):                                     #BFS.
            q, visited, count = [start], set([start]), 0                              #Initialize queue, visited and count.
            while q:                                                                  #Traverse while queue is not empty.
                newq = []                                                             #Initialize new queue.
                for x in q:                                                           #Traverse current nodes in queue.
                    if edges[x] != -1 and edges[x] not in visited:                    #If the out going node exists and is not visited, add it to new queue and visited.
                        newq.append(edges[x])
                        visited.add(edges[x])
                    distance[x] = count                                               #Set the distance from current node to start node to be count.
                q = newq                                                              #Replace q with newq.
                count += 1                                                            #Increase count.
        
        BFS(node1, distance1)                                                         #Start BFS from node1.
        BFS(node2, distance2)                                                         #Start BFS from node2.
        index, minMaxDistance = -1, 100001                                            #Initialize index and minimum of max distances between nodes.
        for i in range(len(edges)):                                                   #Traverse 2 distances.
            if minMaxDistance > max(distance1[i], distance2[i]):                      #If the max distance is greater than minMaxDistance, update minMaxDistance and index.
                minMaxDistance = max(distance1[i], distance2[i])
                index = i
        return index                                                                  #Return index.
