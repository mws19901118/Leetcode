class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])                                                                                                                      #Get the dimensions.
        pacific, atlantic = [(0, i) for i in range(n)] + [(i, 0) for i in range(1, m)], [(m - 1, i) for i in range(n)] + [(i, n - 1) for i in range(m - 1)]     #Get the cells adjacent to pacific and atlantic respectively.
        def bfs(input: List[Tuple[int]]) -> Set:                                                                                                                #BFS and return all visited cells.
            visited = set(input)
            dq = deque(input)
            while dq:
                x, y = dq.popleft()
                for u, v in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:
                    if u < 0 or u >= m or v < 0 or v >= n or heights[u][v] < heights[x][y] or (u, v) in visited:
                        continue
                    visited.add((u, v))
                    dq.append((u, v))
            return visited
        return list(bfs(pacific) & bfs(atlantic))                                                                                                               #Return the intersection after converting to list.
