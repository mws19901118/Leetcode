class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        count = 0
        q = [(0, 0)]
        visited = set([(0, 0)])
        while q:                                    #8 direction BFS.
            newq = []
            for u, v in q:
                if (x, y) == (u, v):
                    return count
                for nu, nv in [(u - 2, v + 1), (u - 1, v + 2), (u + 1, v + 2), (u + 2, v + 1), (u + 2, v - 1), (u + 1, v - 2), (u - 1, v - 2), (u - 2, v - 1)]:
                    if (nu, nv) not in visited:
                        visited.add((nu, nv))
                        newq.append((nu, nv))
            q = newq
            count += 1
