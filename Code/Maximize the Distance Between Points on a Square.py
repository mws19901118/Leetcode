class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        line = []                                                        #Flatten the points from the square boundary to a line based on the clockwise distance from (0, 0) to it.
        for x, y in points:                                              #Traverse points.
            if not x:                                                    #If point is on the left boundary, the distance is y.
                line.append(y)
            elif y == side:                                              #If point is on the top bounday, the distance is side + x.
                line.append(side + x)
            elif x == side:                                              #If point is on the right bounday, the distance sis 3 * side - y.
                line.append(3 * side - y)
            else:                                                        #If point is on the bottom bounday, the distance sis 4 * side - x.
                line.append(4 * side - x)
        line.sort()                                                      #Sort point distances.

        @cache                                                           #Cache the result.
        def canSelect(distance: int) -> bool:                            #Determine if possible to select k points with given min distance.
            for x in line:                                               #Traverse points in line.
                end = x + side * 4 - distance                            #The last point can't be greater than x + side * 4 - distance.
                curr = x
                for _ in range(k - 1):                                   #Iterate k - 1 times.
                    index = bisect_left(line, curr + distance)           #Binary search for the index of next point.
                    if index == len(line) or line[index] > end:          #If no such point or it is greater than end, set cuur to -1 and break.
                        curr = -1
                        break
                    curr = line[index]                                   #Update curr.
                if curr >= 0:                                            #If curr is greater than 0, there is a valid selection, so return true.
                    return True
            return False                                                 #Return false at the end.

        start, end = 0, side * 4                                         #Binary search from 0 to side * 4 to find the maximized min distance.
        while start <= end:
            mid = (start + end) // 2
            if canSelect(mid) and not canSelect(mid + 1):
                return mid
            elif not canSelect(mid):
                end = mid - 1
            else:
                start = mid + 1
