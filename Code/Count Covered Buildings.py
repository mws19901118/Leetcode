class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        minX, maxX, minY, maxY = defaultdict(lambda:inf), defaultdict(lambda:-inf), defaultdict(lambda:inf), defaultdict(lambda:-inf)    #Store the min and max X for each y and min and max Y for each X.
        for x, y in buildings:                                                                                                           #Traverse buildings.
            minX[y] = min(minX[y], x)                                                                                                    #Update minX[y].
            maxX[y] = max(maxX[y], x)                                                                                                    #Update maxX[y].
            minY[x] = min(minY[x], y)                                                                                                    #Update minY[x].
            maxY[x] = max(maxY[x], y)                                                                                                    #Update maxY[x].
        return sum(int(minX[y] < x < maxX[y] and minY[x] < y < maxY[x]) for x, y in buildings)                                           #Count the number of buildings whose x and y are both not on the edge then return.
