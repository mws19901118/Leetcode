class Solution:
    def BFS(self, matrix: List[List[int]], q: set) -> set:
        m, n = len(matrix), len(matrix[0])                                                                              #BFS and return all visited coordinates.
        visited = set()
        while q:
            newq = set()
            visited |= q
            for x, y in q:
                for nx, ny in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:
                    if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] >= matrix[x][y] and (nx, ny) not in visited:
                        newq.add((nx, ny))
            q = newq
        return visited
    
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])                                                                              #Get dimensions.
        pacific = self.BFS(matrix, set([(i, 0) for i in range(m)]) | set([(0, i) for i in range(n)]))                   #Get all coordinates where water can flow to Pacific.
        atlantic = self.BFS(matrix, set([(i, n - 1) for i in range(m)]) | set([(m - 1, i) for i in range(n)]))          #Get all coordinates where water can flow to Atlantic.
        return list(pacific & atlantic)                                                                                 #Return the intersection after converting to list.
