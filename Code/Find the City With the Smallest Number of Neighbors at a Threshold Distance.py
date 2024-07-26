class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        matrix = [[inf for _ in range(n)] for _ in range(n)]                                        #Floyd-Warshall Algorithm to calculate the shortest distance between each city.
        for i in range(n):
            matrix[i][i] = 0
        for x, y, w in edges:
            matrix[x][y] = matrix[y][x] = w
        for k, i, j in product(range(n), range(n), range(n)):
            if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]

        minCount, result = n + 1, -1
        for i in range(n):                                                                         #Find the city has smallest neighbors within distance threshold.
            count = sum(int(matrix[i][j] <= distanceThreshold) for j in range(n) if i != j)
            if count <= minCount:
                minCount = count
                result = i
        return result
