class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])                           #Sort points by ending point in ascending order.
        end, count = float('-inf'), 0                               #Initialize the earilist end of ballons bursted by current arrow and arrows count.
        for l, r in points:                                         #Traverse points.
            if l > end:                                             #If the start of current ballon is greater than end, a new arrow is needed and reset end.
                count += 1
                end = r
        return count
