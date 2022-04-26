class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = [[0 for _ in range(len(points))] for _ in range(len(points))]                                           #Build graph, the edge weight between each point is the Manhattan distance.
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                edges[i][j] = edges[j][i] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        visited = set()                                                                                                 #Use a set to store visited poitns.
        pointLabel = [4000001 for _ in range(len(points))]                                                              #Give each point a label, initially a large number than any edge weight.
        pointLabel[0] = 0                                                                                               #Set the point label of 0 to 0.
        while len(visited) < len(points):                                                                               #Iterate until all points are visited.
            point, minLabel = -1, 4000001                                                                               #Find the unvisited point with smallest label.
            for i, x in enumerate(pointLabel):
                if i not in visited and x < minLabel:
                    minLabel = x
                    point = i
            visited.add(point)                                                                                          #Add it to visited.
            for i, x in enumerate(edges[point]):                                                                        #Update the label of neighbors if the edge weight is smaller than current label.
                if i not in visited:
                    pointLabel[i] = min(pointLabel[i], x)
        return sum(pointLabel)                                                                                          #Return sum of labels.
