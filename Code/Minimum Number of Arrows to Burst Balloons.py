class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()                                               #Sort points by starting point in ascending order.
        end, arrows = float('inf'), 1                               #Initialize the earilist end of ballons bursted by current arrow and arrows count.
        for i, p in enumerate(points):                              #Traverse points.
            if p[0] > end:                                          #If the start of current ballon is greater than end, a new arrow is needed and reset end.
                arrows += 1
                end = p[1]
            else:                                                   #Otherwise, just update end.
                end = min(end, p[1])
        return arrows                                               #Return arrows.
