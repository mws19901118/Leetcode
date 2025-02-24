class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adjacent_list = defaultdict(list)                                                                        #Build adjacent list.
        for x, y in edges:
            adjacent_list[x].append(y)
            adjacent_list[y].append(x)
        bob_path = []                                                                                            #Initialize path for bob.
        def dfs(node: int) -> bool:                                                                              #DFS.
            prev = None if not bob_path else bob_path[-1]                                                        #Get the prev node if exists.
            bob_path.append(node)                                                                                #Append current node to bob_path.
            if not node:                                                                                         #If current node is root, return true.
                return True
            for x in adjacent_list[node]:                                                                        #Traverse all neighbors.
                if x != prev and dfs(x):                                                                         #If x is not prev and dfs(x) is true, return true.
                    return True
            bob_path.pop()                                                                                       #Pop bob_path.
            return False                                                                                         #Return false if current node is not on the path.
        
        dfs(bob)                                                                                                 #DFS to find the path for Bob to move to root.
        visited, q = set(), [(0, 0)]                                                                             #Initialize visited and queue with root node and 0 income.
        index, result = 0, -inf                                                                                  #Initialize index to traverse bob_path simultaneously and result to be -inf.
        while q:                                                                                                 #BFS.
            newq = []                                                                                            #Initialize new q.
            for x, income in q:                                                                                  #Traverse all node and income pair in queue.
                new_income = income + amount[x] // (1 + int(index < len(bob_path) and bob_path[index] == x))     #Add amount[x] to income to calculate new income; add half of amount[x] if Bob also traversed to current node at same time.
                visited.add(x)                                                                                   #Mark x as visited.
                if x and len(adjacent_list[x]) == 1:                                                             #If x is not root and it only has 1 neighbor, x is a leaf node.
                    result = max(result, new_income)                                                             #Update result and continue.
                    continue
                for y in adjacent_list[x]:                                                                       #Traverse neighbors of x.
                    if y not in visited:                                                                         #If y is not visited, append it and the new income to newq.
                        newq.append((y, new_income))
            if index < len(bob_path):                                                                            #If index hasn't reached the end, set amount[bob_path[index]] to 0 to mark it as opened by Bob.
                amount[bob_path[index]] = 0
            q = newq                                                                                             #Replace q with newq.
            index += 1                                                                                           #Increase index.
        return result
