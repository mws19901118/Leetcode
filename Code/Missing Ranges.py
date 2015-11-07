class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        result = []
        if len(nums) == 0:                                        #If the list is empty, directly add range from lower to upper.
            if lower == upper:
                result.append(str(lower))
            else:
                result.append(str(lower) + "->" + str(upper))
            return result
        if lower == nums[0] - 1:                                  #Deal with the range between lower and nums[0], if exists.
            result.append(str(lower))
        elif lower < nums[0] - 1:
            result.append(str(lower) + "->" + str(nums[0] - 1))
        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i] + 1:                         #Deal with the range between nums[i] and nums[i + 1], if exists.
                if nums[i + 1] - nums[i] == 2:
                    result.append(str(nums[i] + 1))
                elif nums[i + 1] - nums[i] > 2:
                    result.append(str(nums[i] + 1) + "->" + str(nums[i + 1] - 1))
        if upper == nums[-1] + 1:                                 #Deal with the range between nums[-1] and upper, if exists.
            result.append(str(upper))
        elif upper > nums[-1] + 1:
            result.append(str(nums[-1] + 1) + "->" + str(upper))
        return result
        
