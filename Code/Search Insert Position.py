class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        l=len(nums)
        if l==0 or target<=nums[0]:                         #If nums is empty or target<=nums[0], it should be inserted at index 0.
            return 0
        if target>nums[-1]:                                 #If target>nums[-1], it should be inserted after the last index.
            return l
        start=0
        end=l-1
        while start<=end:
            mid=(start+end)/2
            if target<=nums[mid] and target>nums[mid-1]:    #If target[mid-1]<target<=target[mid], return mid.
                return mid
            elif target>nums[mid]:
                start=mid+1
            else:
                end=mid
