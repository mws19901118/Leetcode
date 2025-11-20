class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], -x[1]))      #Sort the intervals by starting point in asending order then by ending point in desending order.
        remain = [2] * len(intervals)                      #Each interval has 2 points remain to add.
        result = 0
        while intervals:                                   #Iterate while intervals is not empty.
            (x, _), r = intervals.pop(), remain.pop()      #Pop the last interval and the its remain points.
            for p in range(x, x + r):                      #Traverse the first r points in current interval and add them to the overall intersection.
                for i, (_, y) in enumerate(intervals):     #Traverse the rest intervals.
                    if remain[i] and p <= y:               #If it has remain points and its ending point is not smaller than current point p(starting point is definitely not greater than p), decrease its remain by 1.
                        remain[i] -= 1
                result += 1
        return result
