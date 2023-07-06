class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = len(nums) + 1                                    #Initialize length to be larger then length of nums.
        start, end, s = 0, 0, 0                                   #Initialize sliding window nums[start:end] and its sum s.
        while end < len(nums):                                    #Traverse nums.
            while end < len(nums) and s < target:                 #While end is valid and s is smaller than target, add nums[end] to s and move end to the right.
                s += nums[end]
                end += 1
            while s >= target:                                    #While s is larger than or equal to target, update length if end - start is larger, then substract nums[start] from s and move start to the right.
                length = min(length, end - start)
                s -= nums[start]
                start += 1
        return length if length < len(nums) + 1 else 0            #Return length if it's not greater than length of nums; otherwise return 0 because cannot find such subarray.
