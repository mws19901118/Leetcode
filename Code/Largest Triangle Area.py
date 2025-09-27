class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def calculateArea(p0: List[int], p1: List[int], p2: List[int]) -> float:                                    #Calculete triangle area based on coordinates of each point.
            return 0.5 * abs(p0[0] * (p1[1] - p2[1]) + p1[0] * (p2[1] - p0[1]) + p2[0] * (p0[1] - p1[1]))
        return max(calculateArea(*triangle) for triangle in itertools.combinations(points, 3))                      #Enumerate every triagnle and return the max.
