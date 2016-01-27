class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        miss = 1                                      #Indicate the smallest sum in [1, n] that is missing.
        count = 0                                     #Count the total number of patches.
        i = 0                                         #Traverse from start to end.
        while miss <= n:                              #miss should not be greater than n.
            if i < len(nums) and nums[i] <= miss:     #If nums[i] is smaller than or equal to miss, we can build all the sum in [1, miss + nums[i]).
                miss += nums[i]
                i += 1
            else:                                     #Otherwise, we have to add a number at miss. Then we can build all the sum in [1, 2 * miss).
                miss += miss
                count += 1
        return count
