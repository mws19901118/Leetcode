class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        itemToGroups = defaultdict(int)                                                        #Store the group number of each item.
        groupItems = [set() for _ in range(m)]                                                 #Store the items of each group in a set.
        for i, x in enumerate(group):                                                          #Traverse group.
            if x != -1:                                                                        #If item i has a group, update itemToGroups[i] and add i to groupItems[x].
                itemToGroups[i] = x
                groupItems[x].add(i)
            else:                                                                              #Otherwise, create a new group only containing i and increase m.
                itemToGroups[i] = m
                groupItems.append(set([i]))
                m += 1

        def resolveWithinGroup(groupNumber: int) -> List[int]:                                 #Given group number, resolve order within group using topological sort.
            inDegree = defaultdict(int)
            adjacentList = defaultdict(list)
            for x in groupItems[groupNumber]:                                                  #Traverse all items in current group.
                for y in beforeItems[x]:                                                       #Traverse the before items of x.
                    if y in groupItems[groupNumber]:                                           #If y is in same group, create an edge from y to x.
                        inDegree[x] += 1
                        adjacentList[y].append(x)
            result = []
            q = [x for x in groupItems[groupNumber] if inDegree[x] == 0]
            while q:                                                                           #BFS.
                newq = []
                for x in q:
                    result.append(x)
                    for y in adjacentList[x]:
                        inDegree[y] -= 1
                        if not inDegree[y]:
                            newq.append(y)
                q = newq
            return result if len(result) == len(groupItems[groupNumber]) else []              #Return empty list if there is a cycle within group; otherwise return result.

        inDegree = defaultdict(int)                                                           #Resolve the order among groups.
        adjacentList = defaultdict(list)
        edges = set()
        for i, items in enumerate(groupItems):                                                #Traverse all groups.
            for x in items:                                                                   #Traverse all items in current group.
                for y in beforeItems[x]:                                                      #Traverse the before items of x.
                    if itemToGroups[y] != i and (itemToGroups[y], i) not in edges:            #If y is not in same group and no edge exist from y to x, create an edge from y to x.
                        edges.add((itemToGroups[y], i))
                        inDegree[i] += 1
                        adjacentList[itemToGroups[y]].append(i)
        result = []
        q = [x for x in range(m) if inDegree[x] == 0]
        while q:                                                                              #BFS.
            newq = []
            for x in q:
                result.extend(resolveWithinGroup(x))
                for y in adjacentList[x]:
                    inDegree[y] -= 1
                    if not inDegree[y]:
                        newq.append(y)
            q = newq
        return result if len(result) == n else []                                             #Return empty list if not all items are in result; otherwise return result.
