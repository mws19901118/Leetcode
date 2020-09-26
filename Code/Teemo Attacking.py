class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        count, poisonEnd = 0, 0                                       #Count total poisoned time and store the time when poison end.
        for t in timeSeries:
            count += min(duration, t + duration - poisonEnd)          #Count is the min value between duration and the difference betwwen current time and new poison end time.
            poisonEnd = t + duration                                  #Update poison end time.
        return count                                                  #Return count.
