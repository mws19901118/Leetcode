class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        i = 1                                                                                                                     #Find the index of first number which breaks the non-decreasing array.
        while i < len(nums) and nums[i] >= nums[i - 1]:                                                                           #For example array [..., a, b, c, d, ...], from start to b, it's non-decreasing but c < b. We find index of c first.
            i += 1
        if i == len(nums):                                                                                                        #If no such c, directly return true, as the whole array is non-decreasing.
            return True
        j = i + 1                                                                                                                 #Make sure the array from c to end is also non-decreasing.
        while j < len(nums) and nums[j] >= nums[j - 1]:
            j += 1
        return j == len(nums) and (i == 1 or i + 1 == len(nums) or nums[i] >= nums[i - 2] or nums[i + 1] >= nums[i - 1])          #Also, if b is start, we can set b = c;
                                                                                                                                  #if c is end, we can set c = b;
                                                                                                                                  #if c >= a. we can set b = c;
                                                                                                                                  #if d >= b, we can set c = b.
                                                                                                                                  #Only under these 4 conditions can we make the whole array non-decreasing.
