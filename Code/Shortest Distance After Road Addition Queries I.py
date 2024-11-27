class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adjacent_list = defaultdict(list)              #Initialize adjacent list.
        for i in range(n - 1):                         #Each node ecxcept the last one has an edge pointing to the next node.
            adjacent_list[i].append(i + 1)
        
        def BFS() -> int:                              #BFS to find shortest distance from 0 to n - 1.
            q = [0]
            visited = set([0])
            length = 0
            while q:
                newq = []
                for x in q:
                    if x == n - 1:
                        return length
                    for y in adjacent_list[x]:
                        if y not in visited:
                            newq.append(y)
                            visited.add(y)
                q = newq
                length += 1

        result = []
        for x, y in queries:                          #Traverse quries.
            adjacent_list[x].append(y)                #Add a new edge from x to y.
            result.append(BFS())                      #Append to result after BFS.
        return result
