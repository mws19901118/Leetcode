class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        return max(bisect_left(nums, 0), len(nums) - bisect_right(nums, 0))       #Binary search the left most index to insert 0; all numbers left to it, inclusive, are negative.
                                                                                  #Binary search the right most index to insert 0; all numbers right to it, inclusive, are positive.
                                                                                  #Then return the max.
