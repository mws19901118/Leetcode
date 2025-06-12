class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        return max(abs(nums[(i + 1) % len(nums)] - nums[i]) for i in range(len(nums)))            #Check each adjacent pair.
