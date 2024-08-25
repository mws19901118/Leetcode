class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        def bfs(start: List[int], end: List[int]) -> bool:                                                      #BFS to check if can reach from start to end.
            n, limit = 10 ** 6, 19900                                                                           #Initialize n as the size of board and upper limit of blocked area. Since there are at most 200 blocks, the max area it can blocks is they form a diagonal, then form a triangle with 2 boundaires. Then the max area is (1 + 199) * 199 / 2 = 19900.
            dq = deque([tuple(start)])                                                                          #Put start coordinate in a deque.
            visited = set([tuple(start)])                                                                       #Also put the start coordinate in a set to mark it as visited.
            while dq and len(visited) <= limit:                                                                 #BFS while dq is not empty and the visited area is not graeter than the limit.
                x, y = dq.popleft()                                                                             #Popleft from dq.
                if (x, y) == tuple(end):                                                                        #If current coordinate is end, then return true.
                    return True
                for u, v in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:                                   #Traverse four neighbors.
                    if 0 <= u < n and 0 <= v < n and (u, v) not in blocks and (u, v) not in visited:            #If neighbor is valid and not blocks and not visited, append it to dq and mark it as visited.
                        dq.append((u, v))
                        visited.add((u, v))
            return len(visited) > limit                                                                         #Return if there are more visited area than limit, which means start is not blocked.

        blocks = set([(x, y) for x, y in blocked])                                                              #Put blocks in a set.
        return bfs(source, target) and bfs(target, source)                                                      #Return if both source and target is not blocked.
