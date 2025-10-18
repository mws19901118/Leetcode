class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()                                          #Sort nums in ascending order.
        upperBound, count = -inf, 0                          #Initialize the upper bound of transformed numbers and count of distinct number.
        for x in nums:                                       #Traverse nums.
            if x + k > upperBound:                           #If x + k is greater than upper bound, we can transform x to be a unique number.
                upperBound = max(upperBound + 1, x - k)      #Transform x to the smallest possoble value, which is the max of upper bound + 1 and x - k.
                count += 1                                   #Increase count.
        return count
