class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        l=len(nums)
        result=[]
        if l==0:
            return result
        i=0
        while i<l:
            j=1
            while i+j<l and nums[i+j]==nums[i+j-1]+1:                     #While nums[j] in the range beginning at nums[i], j+=1.
                j+=1
            if j==1:
                result.append(str(nums[i]))
            else:
                result.append(str(nums[i])+"->"+str(nums[i+j-1]))
            i+=j
        return result
