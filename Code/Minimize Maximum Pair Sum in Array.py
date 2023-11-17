class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()                                                                    #Sort nums.
        return max(nums[i] + nums[-(i + 1)] for i in range(len(nums) // 2))            #To minimize maximum pair sum, the largest number should pair with the smallest number. So, return the max sum of k-th number from frond and k-th number from back, 0 <= 1 <= len(nums) // 2.
