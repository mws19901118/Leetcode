class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])                                            #Get dimensions.
        q = [(i, j) for i, j in product(range(m), range(n)) if isWater[i][j]]           #Find all water cells.
        visited = set(q)                                                                #Store visited cells.
        height = 0                                                                      #Initialize height.
        result = [[0 for _ in range(n)] for _ in range(m)]                              #Initialize result.
        while q:                                                                        #BFS from water to land.
            newq = []
            for x, y in q:
                result[x][y] = height                                                   #Set the height for current cell.
                for u, v in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:
                    if u < 0 or u >= m or v < 0 or v >= n or (u, v) in visited:
                        continue
                    newq.append((u, v))
                    visited.add((u, v))
            q = newq
            height += 1                                                                 #Increase height for next iteration.
        return result
