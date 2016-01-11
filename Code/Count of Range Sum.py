class Solution(object):
    def dc(self, firstsum, nums, lower, upper, start, end):                   #Find the number of valid ranges from start to end(exclude end).
        mid = (start + end) / 2                                               #Find the mid point.
        if mid == start:                                                      #If the length of range is smaller than 1, return 0.
            return 0
        left = self.dc(firstsum, nums, lower, upper, start, mid)              #Calculate the number of valid ranges in the left half only.
        right = self.dc(firstsum, nums, lower, upper, mid, end)               #Calculate the number of valid ranges in the right half only.
        l = start
        u = start
        cross = 0                                                             #Now find number of valid ranges cross the mid.
        for r in firstsum[mid:end]:                                           #For every possible ending elements in the right half, find the number of valid starting elements.
            while u < mid and r - firstsum[u] > upper:                        #Becase firstsum is sorted, only have to find the left bound and right bound.
                u += 1
            while l < mid and r - firstsum[l] >= lower:
                l += 1
            cross += l - u                                                    #Add the number of starting elements between the left bound and right bound to cross.
        firstsum[start:end] = sorted(firstsum[start:end])                     #Merge sort the left half and right half.
        return left + right + cross                                           #Return the total number.
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        if len(nums) == 0 or lower > upper:
            return 0
        firstsum = [0]                                                      #Precompute the sum of first i elements.
        for i in range(len(nums)):
            firstsum.append(firstsum[-1] + nums[i])
        return self.dc(firstsum, nums, lower, upper, 0, len(firstsum))      #Divide and conquer.
