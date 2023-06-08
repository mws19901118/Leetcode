class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        return bisect_right(nums, target) - bisect_left(nums, target) > len(nums) // 2      #Calculate the count of target by the rightmost index to insert target minus the leftmost index to insert target, then return if it is greater than half of the length.
