class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()                                                                                                       #Sort nums.
        median = nums[len(nums) // 2] if len(nums) & 1 else (nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) // 2        #Calculate the median.
        return sum(abs(x - median) for x in nums)                                                                         #Use median as the target number and calculate total moves.
