class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adjacentList = collections.defaultdict(list)                                        #Build adjacent list based on edges.
        for x, y in edges:
            adjacentList[x].append(y)
            adjacentList[y].append(x)
        
        def dfs(stack: List[int], visited: set[int]) -> (bool, int):                        #DFS.
            apple, count = hasApple[stack[-1]], 0                                           #Initiallize a boolean indicating if there is any apple in the subtree and the time needed to collect all apples in the subtree.
            for x in adjacentList[stack[-1]]:                                               #Traverse all neighbors of the root of current subtree.
                if x in visited:                                                            #If neighbor is visited, skip.
                    continue
                stack.append(x)                                                             #Append x to stack.
                visited.add(x)                                                              #Add x to visited.
                n_apple, n_count = dfs(stack, visited)                                      #Get the result of DFS from neighbor.
                if n_apple:                                                                 #If neighbor has apple, add the n_count + 2 to count and set apple to true.
                    count += n_count + 2
                    apple = True
                visited.remove(x)                                                           #Remove x from visited.
                stack.pop()                                                                 #Pop stack.
            return apple, count                                                             #Return apple and count.
        
        return dfs([0], set([0]))[1]                                                        #Return the time result of DFS from node 0.
