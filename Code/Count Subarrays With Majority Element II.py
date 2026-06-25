class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:    #Same as Count Subarrays With Majority Element I.py
        n = len(nums)
        prefix = [0] * n + [1] + [0] * n
        result, curr, count = 0, 0, n
        for i, x in enumerate(nums):
            if x == target:
                curr += prefix[count]
                count += 1
            else:
                count -= 1
                curr -= prefix[count]
            prefix[count] += 1
            result += curr
        return result
