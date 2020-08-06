class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for x in nums:                      #Because the 1 ≤ a[i] ≤ n (n = size of array), use the a[abs(a[i]) - 1] to record if a[i] has been visited during traverse.
            if nums[abs(x) - 1] < 0:        #If a[abs(a[i]) - 1] is negative, a[i] is already visited, add a[i] to result.
                result.append(abs(x))
            else:                           #Otherwise, change a[abs(a[i]) - 1] to its negative value.
                nums[abs(x) - 1] *= - 1
        return result
