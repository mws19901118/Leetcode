class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()                                                      #Sort nums.
        result = 0                                                       #Initialize result.
        for i, x in enumerate(nums):                                     #Traverse nums.
            left = bisect_left(nums, lower - x, lo = i + 1)              #Binary search the leftmost index to insert lower - x in nums[i + 1].
            right = bisect_right(nums, upper - x, lo = i + 1)            #Binary search the rightmost index to insert upper - x in nums[i + 1],
            result += right - left                                       #The numbers in nums[left:right] can make a fair pair with x.
        return result
