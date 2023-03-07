class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        @cache
        def calculateTrip(limit: int) -> int:                                                                 #Given time limit, calculate total trips can be done and cache result.
            return sum(limit // x for x in time)

        start, end = 1, min(time) * totalTrips                                                                #Binary search between 1 and min(time) * totalTrips.
        while start <= end:
            mid = (start + end) // 2                                                                          #Calculate mid.
            if calculateTrip(mid) >= totalTrips and calculateTrip(mid - 1) < totalTrips:                      #If with mid, we can finish at last totalTrips while with mid - 1, we cannot; then return mid.
                return mid
            elif calculateTrip(mid - 1) >= totalTrips:                                                        #If with mid - 1, we can finish more than totalTrips, set end = mid - 1.
                end = mid - 1
            else:                                                                                             #Otherwise, set start = mid + 1.
                start = mid + 1
