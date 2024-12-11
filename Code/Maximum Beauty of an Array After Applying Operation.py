class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()                                             #Sort nums.
        result, length, left = 0, 0, 0                          #Initialize result, current length and left boundary of sliding window.
        for i, x in enumerate(nums):                            #Traverse nums.
            length += 1                                         #Add x to the sliding window, so increasing the length.
            while left < i and nums[left] < nums[i] - 2 * k:    #While left is smaller than i and nums[left] is smaller than nums[i] - 2 * k, we cannot change nums[left] and nums[i] to same value after opeartions, so decrease length and move forward left.
                left += 1
                length -= 1
            result = max(result, length)                        #Update result if necessary.
        return result
