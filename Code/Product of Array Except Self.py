import math
class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        l=len(nums)
        p=[1]                                 #Record the product of array except self.
        for i in range(1,l):
            p.append(p[i-1]*nums[i-1])        #Calculate the product before each element.
        t=1                                   #Record the product after current element.
        for i in range(l):
            p[l-1-i]*=t                       #The answer equals the product of product before current element and the product after current element.
            t*=nums[l-1-i]                    #Update t.
        return p
