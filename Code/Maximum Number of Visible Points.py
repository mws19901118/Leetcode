class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        pointOnLocation = 0                                                                     #Count the points on location.
        arcs = []                                                                               #Initialize the arcs of each point not on location..
        for x, y in points:                                                                     #Traverse points.
            if x == location[0] and y == location[1]:                                           #If current point is on location, increase pointOnLocation and continue.
                pointOnLocation += 1
                continue
            arcs.append(atan2(x - location[0], y - location[1]))                                #Convert current point to arc by the angle of current line to location and x axis.
        arcs.sort()                                                                             #Sort arcs.
        arc = angle * pi / 180                                                                  #Convert angle to arc.
        for x in arcs:                                                                          #Traverse arcs and app x + 2 * pi for all x <= arc, because we start from x axis but the angle can contain points from both side of x axis. So, now we don't need specially such case.
            if x > arc:
                break
            arcs.append(x + 2 * pi)
        count = 0
        left, right = 0, 0                                                                      #Initialize the left and right boundary of sliding window.
        while right < len(arcs):                                                                #Traverse while right < len(arcs).
            while right < len(arcs) and arcs[right] - arcs[left] <= arc:                        #While acrs[right] - arcs[left] <= arc, move forward right, all pointes in arcs[left:right] can be viewed by angle. 
                right += 1
            count = max(count, right - left)                                                    #Update cound if right - left is greater.
            left += 1                                                                           #Move forward left.
        return count + pointOnLocation                                                          #Return count plus pointOnLocation.
