class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()                                                                  #Sort nums.
        return min(nums[i + k - 1] - nums[i] for i in range(len(nums) - k + 1))      #Find the min difference.
