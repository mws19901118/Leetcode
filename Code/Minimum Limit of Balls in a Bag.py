class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        @cache                                                                         #Cache result.
        def divide(limit: int) -> int:                                                 #Calculate the number of operations needed to divide all numbers to be not greater than limit.
            return inf if not limit else sum(ceil(x / limit) - 1 for x in nums)        #If limit is 0, return inf; otherwise, return the sum of ceil(x / limit) - 1 for all x in numbers.

        start, end = 1, max(nums)                                                      #Binary search from 1 to max(nums).
        while start <= end:
            mid = (start + end) // 2
            if divide(mid) <= maxOperations and divide(mid - 1) > maxOperations:
                return mid
            elif divide(mid) > maxOperations:
                start = mid + 1
            else:
                end = mid - 1
