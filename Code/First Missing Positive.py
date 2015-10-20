class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        l=len(nums)
        for i in range(l):
            while nums[i]!=i+1 and nums[i]>0 and nums[i]<=l and nums[i]!=nums[nums[i]-1]:  #To make nums[i] equals i+1, while nums[i]!=i+1, sawp nums[i] and nums[nums[i] - 1](Satisfy 0<=nums[i]-1<n and nums[i]!nums[nums[i]-1]).
                temp=nums[nums[i] - 1]
                nums[nums[i] - 1]=nums[i]
                nums[i]=temp
        
        for i in range(l):
            if nums[i]!=i+1:                                                               #If nums[i]!=i+1, i+1 is missing.
                return i+1
                
        return l+1                                                                         #If can't find missing positive integer, the result is the first positive integer out of range, i.e. len(nums)+1.
