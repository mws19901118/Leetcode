class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adjacentList = collections.defaultdict(list)                                        #Build adjacent list based on edges.
        for x, y in edges:
            adjacentList[x].append(y)
            adjacentList[y].append(x)
        
        def dfs(curr: int, prev: int) -> (bool, int):                                       #DFS.
            apple, count = hasApple[curr], 0                                                #Initiallize a boolean indicating if there is any apple in the subtree and the time needed to collect all apples in the subtree.
            for x in adjacentList[curr]:                                                    #Traverse all neighbors of the root of current subtree.
                if x == prev:                                                               #If x is same as prev, it's visited, so skip.
                    continue
                n_apple, n_count = dfs(x, curr)                                             #Get the result of DFS from neighbor.
                if n_apple:                                                                 #If neighbor has apple, add the n_count + 2 to count and set apple to true.
                    count += n_count + 2
                    apple = True
            return apple, count                                                             #Return apple and count.
        
        return dfs(0, -1)[1]                                                                #Return the time result of DFS from node 0.
    
