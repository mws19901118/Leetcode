class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        maxVInLeft, maxV = nums[0], nums[0]       #Initialize the max value in left and max value in whole array.
        result = 1                                #Initialize length of left.
        for i, x in enumerate(nums):              #Traverse nums.
            if x < maxVInLeft:                    #If x < maxInLeft, include x in left and update the max value in left to be the max value so far.
                result = i + 1
                maxVInLeft = maxV
            else:                                 #Otherwise, update maxV.
                maxV = max(maxV, x)
        return result                             #Return result.
