class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy:                                                        #If start and finish are same, t cannot be 1.
            return t != 1
        distanceX, distanceY = abs(sx - fx), abs(sy - fy)                                #Get the distance on X axis and distance on Y axis.
        minTimeRequired = min(distanceX, distanceY) + abs(distanceX - distanceY)         #Min time required is min(distanceX, distanceY)(move diagonally first) + abs(distanceX - distanceY)(then move straight).
        return minTimeRequired <= t                                                      #Return if minTimeRequired is not greater than t.
