class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adjacenetList = defaultdict(list)
        for x, y in connections:                                                                          #Build the adjacent list.
            adjacenetList[y].append((x, False))                                                           #If it's an in edge to y, tag the edge as false for y.
            adjacenetList[x].append((y, True))                                                            #If it's an out edge from x, tag the edge as true for x.
        
        def DFS(prev: int, curr: int) -> int:                                                             #DFS.
            return sum(DFS(curr, x) + int(flag) for x, flag in adjacenetList[curr] if x != prev)          #Return the sum of edges need to reorder from curr. So, for each edge of curr and destination is not prev, reorder it if it is an out edge.

        return DFS(None, 0)                                                                               #Return the result of DFS from 0.
