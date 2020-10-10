class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()                                             #Sort points by starting point ascending ly.
        count, i = 0, 0                                           #Initialize count to be 0 and pointer i to start from 0.
        while i < len(points):
            j, end = i + 1, points[i][1]                          #Initialize pointer j to start from i + 1, and common end to be the end of points[i].
            while j < len(points) and points[j][0] <= end:        #If points[j]'s start is not greater than common end, a single arrow can burst from points[i] to points[j].
                end = min(end, points[j][1])                      #Update common end to be the smallest end from points[i] to points[j].
                j += 1                                            #Move j to next.
            count += 1                                            #Add 1 to count.
            i = j                                                 #Move i to j.
        return count
