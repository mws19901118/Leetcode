class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = bisect_left(nums, target)                                #Binary search for the first position.
        if first == len(nums) or nums[first] != target:                  #If it is invalid and the number on it is not target, set it to -1.
            first = -1
        last = bisect_right(nums, target) - 1                            #Binary search for the last position.
        if last < 0 or nums[last] != target:                             #If it is invalid and the number on it is not target, set it to -1.
            last = -1
        return [first, last]                                             #Return [first, last].
