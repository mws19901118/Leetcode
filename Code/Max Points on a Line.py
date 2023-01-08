class Solution:
    def formLine(self, x1: int, y1: int, x2: int, y2: int) -> (float, float):
        if x1 == x2:                                                            #If x1 == x2, k is infinity and b is x1.
            return (float('inf'), x1)
        else:                                                                   #Otherwise k is (y1 - y2) / (x1 - x2), and b is y1 - k * x1.
            k = (y1 - y2) / (x1 - x2)
            b = y1 - k * x1
            return (k, b)

    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:                                                    #If there is only one point, return 1.
            return 1
        pointsOnLine = collections.defaultdict(set)                             #Store the points on a line.
        for i, (x, y) in enumerate(points):                                     #Traverse points.
            for u, v in points[i + 1:]:                                         #Traverse points[i + 1:].
                k, b = self.formLine(x, y, u, v)                                #Calculate the k and b for the link y = kx + b formed by (x, y) and (nx, ny)
                pointsOnLine[(k, b)].add((x, y))                                #Add (x, y) to the line.
                pointsOnLine[(k, b)].add((u, v))                                #Add (u, v) to the line.
        return max(len(p) for p in pointsOnLine.values())                       #Return the max count of points of lines.
