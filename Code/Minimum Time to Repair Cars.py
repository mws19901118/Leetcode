class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        @cache                                                              #Cache result.
        def canRepair(limit: int) -> bool:                                  #Determine if cars can be repaired with limit minutes.
            return sum(floor(sqrt(limit / r)) for r in ranks) >= cars       #Basically sum up floor(sqrt(limit / r)) for each r in ranks then check if the sum is at least cars; because r * x ** 2 <= limit then x <= squr(limit / r) and x has to be an integer. 
            
        start, end = 1, cars * cars * min(ranks)                            #Binary search from 1 to sum(candies).
        while start <= end:
            mid = (start + end) // 2                                        #Calculate the mid.
            if canRepair(mid) and not canRepair(mid + 1):                   #If can repair with mid minutes but cannot repair with mid - 1 minutes, mid is the min time, so return mid.
                return mid
            elif canRepair(mid - 1):                                        #If can repair with mid - 1 minutes, keep binary search from start to mid - 1.
                end = mid - 1
            else:                                                           #Otherwise, keep binary search from mid + 1 to end.
                start = mid + 1
