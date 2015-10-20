class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        l=len(nums)
        end=l-1
        start=0
        while start<=end:
            if nums[start]==val:            #If nums[start] equals val, swap it with nums[end].
                temp=nums[start]
                nums[start]=nums[end]
                nums[end]=temp
                end-=1
            else:                           #If nums[start] does not equal val, start+=1.
                start+=1
        return end+1                        #Return end+1.
