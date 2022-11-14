class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rows, columns = defaultdict(set), defaultdict(set)                  #Store the stones by rows and columns.
        for x, y in stones:                                                 #Treat them as a graph: each stone is a node and if 2 stones are in same row or column, there is an edge linking them.
            rows[x].add(y)
            columns[y].add(x)
        count = 0                                                           #Initialize the overall count of stones to remove.
        for s in stones:                                                    #Traverse stones. For each connected component in graph, we can remove them until there is only one node left.
            group = 0                                                       #Initialize the stones count for current connected component.
            stack = [s]                                                     #Pushing current stone to stack.
            while stack:                                                    #DFS while stack is not empty.
                x, y = stack.pop()                                          #Pop top of stack.
                if y not in rows[x] or x not in columns[y]:                 #If y not in rows[x] or x not in columns[y], then stone is already removed.
                    group = max(group, 1)                                   #Set the group count to at least 1, handling the case that the initial stone of this group is already removed, and continue DFS.
                    continue
                rows[x].remove(y)                                           #Remove stone, removintg y from rows[x] and x from columns[y].
                columns[y].remove(x)
                for ny in rows[x]:                                          #For all the neighbors in rows[x], append [x, ny] to stack.
                    stack.append([x, ny])
                for nx in columns[y]:                                       #For all the neighbors in columns[y]. append [nx, y] to stack.
                    stack.append([nx, y])
                group += 1                                                  #Increase group count.
            count += group - 1                                              #Update overall count.
        return count                                                        #Return.
