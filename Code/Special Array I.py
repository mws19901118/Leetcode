class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        return all((nums[i] & 1) ^ (nums[i + 1]) & 1 for i in range(len(nums) - 1))      #The XOR result of last bits of each adjacent pair should be 1.
