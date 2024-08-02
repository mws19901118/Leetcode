class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total = sum(nums)                                    #Count total 1s.
        count, result = sum(nums[:total]), len(nums)         #Count the 1s in nums[:total].
        result = total - count                               #Initialize result to be the number of swaps to move all 1 to nums[:total].
        for i in range(len(nums) - 1):                       #Traverse nums to move sliding window forward.
            count -= nums[i]                                 #Move nums[i] out of sliding window.
            count += nums[(i + total) % len(nums)]           #Move nums[(i + total) % len(nums)] into sliding window.
            result = min(result, total - count)              #Calculate the number of swaps to move all 1 to the sliding window and update result if necessary.
        return result
