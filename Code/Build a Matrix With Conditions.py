class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topoSort(edges: List[List[int]]) -> List[int]:                                                                                    #Topolofical sort to get the order of either row or column.
            adjacentList = defaultdict(list)                                                                                                  #Build adjacent list.
            for x, y in edges:
                adjacentList[x].append(y)
            order = []                                                                                                                        #Initialize order.
            visited = [0] * (k + 1)                                                                                                           #Mark the visit status of each node.
            for i in range(1, k + 1):                                                                                                         #Traverse each node.
                if not visited[i] and dfs(i, adjacentList, visited, order):                                                                   #If node is unvisited, start a DFS.
                    return []                                                                                                                 #Return empty list if there is any cycle.
            order.reverse()                                                                                                                   #Reverse order to get the correct order.
            return order

        def dfs(node: int, adjacentList: defaultdict, visited: List[int], order: List[int]) -> bool:                                          #DFS to determine topological order and return if there is any cycle.
            visited[node] = 1                                                                                                                 #Mark node as visiting.
            for neighbor in adjacentList[node]:                                                                                               #Traverse neighbors of current node.
                if not visited[neighbor] and dfs(neighbor, adjacentList, visited, order):                                                     #If neighbor is unvisited, keep dfs recursively and return true if there is any cycle.
                    return True
                elif visited[neighbor] == 1:                                                                                                  #If neighbor is visiting, return true because there is a cycle now.
                    return True
            visited[node] = 2                                                                                                                 #Mark node as visited.
            order.append(node)                                                                                                                #Add node to the order.
            return False                                                                                                                      #Return false.

        rowOrders, columnOrders = topoSort(rowConditions), topoSort(colConditions)                                                            #Get the row order and column oder.
        if not rowOrders or not columnOrders:                                                                                                 #If either order is empty, there is a cycle, so return emoty matrix.
            return []
        matrix = [[0 for _ in range(k)] for _ in range(k)]                                                                                    #Initialize matrix.
        rowPositions, columnPositions = {num: i for i, num in enumerate(rowOrders)}, {num: i for i, num in enumerate(columnOrders)}           #Transform order to position of each number, in row and column respectively.
        for x in range(1, k + 1):                                                                                                             #Traverse from 1 to k.
            matrix[rowPositions[x]][columnPositions[x]] = x                                                                                   #Put x on matrix on its row position and column position.
        return matrix
