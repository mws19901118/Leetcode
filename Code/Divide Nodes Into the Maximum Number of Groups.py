class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adjacent_list = defaultdict(list)                                                     #Build graph.
        for x, y in edges:
            adjacent_list[x].append(y)
            adjacent_list[y].append(x)
        component, max_nodes = {}, defaultdict(lambda: -1)                                    #Store which component each node belongs to and the max nodes in each component(initially -1).
        
        def BFS(node: int, component_id: int) -> int:                                         #BFS with node and component_id to calculate the max depth of tree with node as the tree root.
            q = deque([(node, 1)])                                                            #Initialize q with node and level 1.
            depth = {node: 1}                                                                 #Store the depth of each node in current BFS.
            max_depth = 0                                                                     #Store the max_depth in current BFS.
            while q:                                                                          #BFS while q is not empty.
                x, level = q.popleft()                                                        #Pop the node and its level from the queue.
                for y in adjacent_list[x]:                                                    #Traverse neighbors of x.
                    if y not in depth:                                                        #If y is not visited in current BFS, set its level to level + 1 and append y and level + 1 to queue.
                        depth[y] = level + 1
                        q.append((y, depth[y]))
                        component[y] = component_id                                           #Also set component[y] to current component id(this operation is idempotent).
                    elif abs(depth[y] - level) != 1:                                          #Otherwise, if the abs between levels[y] and current level is not 1, return -1 because it violates the valid condition.
                        return -1
                max_depth = max(max_depth, level)                                             #Update max_depth.     
            return max_depth                                                                  #Return max_depth after BFS.
        
        id = 0                                                                                #Initialize component id to 0.
        for i in range(1, n + 1):                                                             #Traverse each node.
            if i not in component:                                                            #If current node is not in component, assign current id to it and increase id.
                component[i] = id
                id += 1
            max_nodes[component[i]] = max(max_nodes[component[i]], BFS(i, component[i]))      #BFS from current node and its component id; then update the max nodes of current component. Basically try each node as root and find the max depth.
            if max_nodes[component[i]] == -1:                                                 #If the max nodes of current component is still -1, current component is invalid, so return -1.
                return -1
        return sum(max_nodes.values())                                                        #Return the sum of max nodes of all components.
