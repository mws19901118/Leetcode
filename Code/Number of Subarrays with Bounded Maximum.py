class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        count, start, last = 0, -1, -1      #Initialize subarrays count, index of last integer greater than right and index of last number within range and after start.
        for i, x in enumerate(nums):        #Traverse nums.
            if right < x:                   #If x is greater than right, update start and last.
                start = i
                last = i
            elif left <= x <= right:        #If x is within range, any subarray starting within nums[start + 1:i + 1] and ending at i has bounded maximum.
                last = i                    #Update last.
                count += i - start
            else:                           #If x is smaller than left, any subarray starting within nums[start + 1:last + 1] and ending at i has bounded maximum.
                count += last - start
        return count
