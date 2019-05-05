class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        min1, min2 = 1001, 1001
        max1, max2, max3 = -1001, -1001, -1001
        for x in nums:                                        #Find the largest 3 numbers and smallest 2 numbers in a single pass.
            if x > max1:
                max1, max2, max3 = x, max1, max2
            elif x > max2:
                max2, max3 = x, max2
            elif x > max3:
                max3 = x
            if x < min1:
                min1, min2 = x, min1
            elif x < min2:
                min2 = x
        return max(max1 * max2 * max3, min1 * min2 * max1)    return the max of max1 * max2 * max3 and min1 * min2 * max1. Because if min1 and min2 are negative while max1 is positive, min1 * min2 * max1 could be larger than max1 * max2 * max3. 
