class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] != i + 1 and nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:   #To make nums[i] equals i + 1, while nums[i] != i + 1, sawp nums[i] and nums[nums[i] - 1](Satisfy 0 <= nums[i] - 1 < n and nums[i] != nums[nums[i] - 1]).
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        for i in range(len(nums)):
            if nums[i] != i + 1:                                                                                #If nums[i] != i + 1, i + 1 is missing.
                return i + 1
            
        return len(nums) + 1                                                                                    #If can't find missing positive integer, the result is the first positive integer out of range, i.e. len(nums)+1.
