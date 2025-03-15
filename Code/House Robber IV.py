class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        @cache                                                    #Cache result.
        def canRob(capacity: int) -> bool:                        #Determine if the robber can rob successfully with current capacity.
            length, count = 0, 0                                  #Initialize length of contiguous subarray of houses whose money is not greater than capacity; also initialize count of houses can be robbed.
            for i in range(len(nums) + 1):                        #Traverse from 0 to len(nums).
                if i == len(nums) or nums[i] > capacity:          #If i is len(nums) or nums[i] is greater than capacity, add (length + 1) // 2 to count because the robber cannot rob adjacent houses.
                    count += (length + 1) // 2
                    length = 0                                    #Reset length.
                else:                                             #Otherwise, increase length.
                    length += 1
            return count >= k                                     #Return if count is at least k.

        start, end = min(nums), max(nums)                         #Binary search between the min value and max value in nums.
        while start <= end:
            mid = (start + end) // 2                              #Calculate the mid.
            if canRob(mid) and not canRob(mid - 1):               #If the robber can rob with mid as capacity but cannot with mid - 1 as capacity, mid is the min capacity so return mid.
                return mid
            elif canRob(mid - 1):                                 #If the robber can rob with mid - 1, keep binary search from start to mid - 1.
                end = mid - 1
            else:                                                 #Otherwise, keep binary search from mid + 1 to end.
                start = mid + 1
