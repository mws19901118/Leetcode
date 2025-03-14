class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        @cache                                                  #Cache result.
        def canAllocate(limit: int) -> bool:                    #Determine if candies can be divided to k children with each child allocated with limit candies.
            return sum(x // limit for x in candies) >= k        #Basically sum up x // limit for each x in nums then check if the sum is not smaller than k.
            
        start, end = 1, sum(candies)                            #Binary search from 1 to sum(candies).
        while start <= end:
            mid = (start + end) // 2                            #Calculate the mid.
            if canAllocate(mid) and not canAllocate(mid + 1):   #If can allocate with mid candies per kid but cannot allocate with mid + 1 candies per kid, mid is the max candies, so return mid.
                return mid
            elif canAllocate(mid + 1):                          #If can allocate with mid + 1 candies, keep binary search from mid + 1 to end.
                start = mid + 1
            else:                                               #Otherwise, keep binary search from start to mid - 1.
                end = mid - 1
        return 0                                                #Return 0 if cannot allocate.
