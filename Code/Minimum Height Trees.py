class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        degree = [0 for i in range(n)]                                                              #Store the degree of each node.
        adjacentList = [[] for i in range(n)]                                                       #Store the adjacent list of each node.
        for s, e in edges:                                                                          #Construct degree and adjacent list.
            degree[s] += 1
            degree[e] += 1
            adjacentList[s].append(e)
            adjacentList[e].append(s)
        q = set([i for i in range(n) if degree[i] <= 1])                                            #Find all the nodes whose degree is not larger than 1. 
        result = set()
        while q:                                                                                    #Start BFS.
            newq = set()
            for x in q:                                                                             #For each node in queue, traverse all its neighbor in adjacent list.
                for y in adjacentList[x]:
                    degree[y] -= 1                                                                  #Minus 1 to the neighbor's degree.
                    if degree[y] == 1:                                                              #If neighbor's degree is 1, add it to the new queue.
                        newq.add(y)
            result = q                                                                              #Always store current queue in result.
            q = newq                                                                                #Replace current queue with new queue.
        return list(result)                                                                         #Return result after converting it to list.
