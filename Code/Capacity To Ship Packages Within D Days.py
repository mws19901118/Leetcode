class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        @cache                                                              #Cache result.
        def getDays(capacity: int) -> int:                                  #Get the days needed to ship with given capacity.
            total, count = 0, 0                                             #Initialize the total weight of current day and count of days.
            for i, x in enumerate(weights):                                 #Traverse weights.
                if total + x > capacity:                                    #If cannot ship with x in current day, increase count of days and reset total.
                    count += 1
                    total = 0
                total += x                                                  #Ship x and add x to total.
            return count + int(total > 0)                                   #If there are packages for current day, increase count, then return.

        start, end = max(weights), sum(weights)                             #Start binary search from max of weights to sum of weights.
        while start <= end:
            mid = (start + end) // 2                                        #Calculate mid.
            if getDays(mid) <= days and getDays(mid - 1) > days:            #If can ship within days with mid as capacity and cannot ship within days with mid - 1 as capacity, return mid.
                return mid
            elif getDays(mid) > days:                                       #If cannot ship within days with mid as capacity, min capacity is greater than mid, so continue binary search from mid + 1 to end.
                start = mid + 1
            else:                                                           #Otherwise, min capacity is smaller than mid, so continue binary search from start to mid - 1.
                end = mid - 1
        return start
