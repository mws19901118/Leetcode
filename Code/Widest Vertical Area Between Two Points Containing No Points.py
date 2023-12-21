class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()                                                                      #Sort points.
        return max(points[i][0] - points[i - 1][0] for i in range(1, len(points)))         #Return the max diff on x coordinate between each adjacent pair of points.
