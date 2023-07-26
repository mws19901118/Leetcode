class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        @cache                                                                            #Cache result.
        def totalHour(speed: int) -> int:                                                 #Calculate total hours needed with given speed.
            return sum(ceil(x / speed) for x in dist[:-1]) + dist[-1] / speed             #Sum up hours(round up except for the last one).

        start, end = 1, 10 ** 7                                                           #Initialize start and end.
        while start <= end:                                                               #Binary search.
            mid = (start + end) // 2
            if totalHour(mid) <= hour and (mid == 1 or totalHour(mid - 1) > hour):        #If total hour for mid is not greater than required hour and mid is 1 or total hour for mid - 1 is greater than required hour, mid is the minimum speed.
                return mid
            elif totalHour(mid) > hour:                                                   #If total hour for mid is greater than required hour, binary search from mid + 1 to end.
                start = mid + 1
            else:                                                                         #Otherwise, binary search from start to mid - 1.
                end = mid - 1
        return -1                                                                         #Return -1 if cannot found such speed.
