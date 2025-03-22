class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacentList = [[] for _ in range(n)]                                               #Build adjacent list.
        for x, y in edges:
            adjacentList[x].append(y)
            adjacentList[y].append(x)
        visited = set()                                                                     #Store visited nodes.
        result = 0
        for i in range(n):                                                                  #Traverse each node
            if i in visited:                                                                #If i is already visited, skip.
                continue
            visited.add(i)                                                                  #Mark i as visited.
            component = []                                                                  #Store the nodes of current component.
            q = deque([i])                                                                  #Put i in a deque.
            while q:                                                                        #BFS to find all nodes in current component.
                x = q.popleft()
                component.append(x)
                for y in adjacentList[x]:
                    if y not in visited:
                        q.append(y)
                        visited.add(y)
            result += all(len(adjacentList[x]) == len(component) - 1 for x in component)    #Increase result if all nodes have len(component) - 1 neighbors in adjacent list.
        return result
