class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        if len(graph) == 1:                                             #If there is only one node, return 0.
            return 0
        endingState = (1 << len(graph)) - 1                             #Use a bit mask to represent which node is visited; when all nodes are visited, the bit mask is all 1.
        masks = [1 << i for i in range(len(graph))]                     #Generate the bit masks for visiting each node, basically the bit at that node is 1, other bits are 0.
        queue = [(i, masks[i]) for i in range(len(graph))]              #Use a queue to store current node and mask, starting simultaneously from all nodes.
        seen = set(queue)                                               #Use a set to store seen nodes and mask combination.

        steps = 0
        while queue:                                                    #Start BFS.
            nextq = []                                                  #Initialize queue for next iteration.
            for node, mask in queue:                                    #Traverse queue.
                for neighbor in graph[node]:                            #Traverse all neighbors of current node.
                    nextMask = mask | masks[neighbor]                   #Update bit mask for all visited nodes.
                    if nextMask == endingState:                         #If all nodes visited, return steps + 1.
                        return 1 + steps
                    if (neighbor, nextMask) not in seen:                #If the combination of neightbor and nextMask is not see, add it to seen and nextq.
                        seen.add((neighbor, nextMask))
                        nextq.append((neighbor, nextMask))
            steps += 1                                                  #Increase steps.
            queue = nextq                                               #Replace queue with nextq.
