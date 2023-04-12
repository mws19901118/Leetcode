class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()                                                                                                #Sort intervals in ascending order.
        return all(intervals[i][1] <= intervals[i + 1][0] for i in range(len(intervals) - 1))                           #Return all interval's ending time is not greater than next intervals's starting time.
