class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adjacentList = collections.defaultdict(list)                                  #Build the adjacent list.
        for x, y in edges:
            adjacentList[x].append(y)
            adjacentList[y].append(x)
        result = [0] * n                                                              #Initialze the result to be 0 for all nodes.

        def DFS(stack: List[int], visited: set[int]) -> collections.Counter:
            count = collections.Counter()                                             #Initialize a counter.
            count[labels[stack[-1]]] = 1                                              #The node count of current label is 1.
            for x in adjacentList[stack[-1]]:                                         #Traverse neighbors.
                if x in visited:                                                      #If neighbor is visited, skip.
                    continue
                stack.append(x)                                                       #Append neighbor to stack.
                visited.add(x)                                                        #Mark neighbor as visited.
                for k, v in DFS(stack, visited).items():                              #Traverse the DFS result from neighbor.
                    count[k] += v                                                     #Add all count of node to current counter.
                visited.remove(x)                                                     #Remove neighbor from visited.
                stack.pop()                                                           #Pop stack.
            result[stack[-1]] = count[labels[stack[-1]]]                              #Set the result for current node.
            return count                                                              #Return counter.

        DFS([0], set([0]))                                                            #DFS from node 0.
        return result
