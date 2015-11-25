# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        def cmpInterval(a, b):                              #Customize cmp method for Interval.
            return a.start - b.start
        intervals.sort(cmp = cmpInterval)
        l = len(intervals)
        for i in range(l - 1):                              #Find overlap one by one.
            if intervals[i].end > intervals[i + 1].start:
                return False
        return True
