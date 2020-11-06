class Solution:
    def sumDivision(self, nums: List[int], divisor: int) -> int:                    #Calculate the sum of division for given divisor.
        return sum(ceil(x / divisor) for x in nums)
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        start, end = 1, max(nums)                                                   #Start binary search between 1 and max value in nums.
        while start <= end:
            mid = (start + end) // 2
            x = self.sumDivision(nums, mid)                                         #Calculate sum of division for mid.
            if x > threshold:                                                       #If the sum is greater than threshold, set start = mid + 1.
                start = mid + 1
            elif mid == 1 or self.sumDivision(nums, mid - 1) > threshold:           #Else if mid is 1 or the sum of division for (mid - 1) is greater than threshold, return mid.
                return mid
            else:                                                                   #Otherwise, set end = mid - 1.
                end = mid - 1
