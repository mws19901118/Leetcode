class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        sum=0
        length=len(nums)
        minl=length+1                                 #Record the minimal subarray length.
        start=0
        end=0
        while not (start>=length and sum<s):          #If current sum is smaller than s, the start pointer will move forward, but we have to prevent it from stepping out of border.
            if sum<s:
                sum+=nums[start]                      #If current sum is smaller than s, add nums[start] to sum and move forward start pointer.
                start+=1
            else:                                     #If current sum is larger than or equal to s, delete nums[end] from sum and move forward end pointer.
                if start-end<minl:                    #If length of current subarray whose sum is larger than or equal to s, update the minimal subarray length if necessary.
                    minl=start-end
                sum-=nums[end]
                end+=1
        
        if minl==length+1:                            #If minimal subarray length is larger than length of the whole array, no subarray satisfies the requirement.
            return 0
        else:
            return minl
