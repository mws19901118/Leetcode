class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        l=len(nums)
        ranges=-1                                                 #Record the index at which target first appears.
        rangee=-1                                                 #Record the index at which target last appears.
        
        if target==nums[0]:
            ranges=0
        else:
            start=0
            end=l-1
            while start<=end:
                mid=(start+end)/2
                if target==nums[mid] and target>nums[mid-1]:      #Binary search for ranges.
                    ranges=mid
                    break
                elif target>nums[mid]:
                    start=mid+1
                else:
                    end=mid-1
        if ranges==-1:                                            #If can't find ranges, then can't find rangee either.
            rangee=-1
        elif target==nums[-1]:
            rangee=l-1
        else:
            start=0
            end=l-1
            while start<=end:
                mid=(start+end)/2
                if target==nums[mid] and target<nums[mid+1]:      #Binary search for rangee.
                    rangee=mid
                    break
                elif target<nums[mid]:
                    end=mid-1                
                else:
                    start=mid+1
                
        return [ranges, rangee]
