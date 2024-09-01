class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        index, distance = -1, inf                                              #Initialize index and distance.
        for i, (u, v) in enumerate(points):                                    #Traverse points.
            if (u == x or v == y) and abs(u - x) + abs(v - y) < distance:      #If current point share same x or y coordinates and the manhattan distance is smaller, update index and distance.
                distance = abs(u - x) + abs(v - y)
                index = i
        return index
