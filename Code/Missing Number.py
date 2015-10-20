class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = max(nums)               #Get the max value of the list.
        s0 = sum(nums)              #Calculate the actual sum if the list.
        s1 = n * (n + 1) / 2        #Calculate the should-be sum without missing number. 
        if s0 == s1:                #if the 2 sums are equal, there are 2 cases.
            if 0 in nums:           #If 0 is in the list, no number is missing, return the next number.
                return n + 1
            else:                   #If 0 is not in the list, 0 is missing, return 0.
                return 0
        return s1 - s0              #Otherwise, return the difference between s1 and s2.
