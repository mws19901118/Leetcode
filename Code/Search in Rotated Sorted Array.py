class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:                                                                                        #If found target, return mid.
                return mid
            if nums[0] <= nums[mid] < target or nums[mid] < target <= nums[-1] or target < nums[0] <= nums[mid]:           #1. If nums[mid] is smaller than target and both nums[mid] and target is on same slope, target is in the second half(between mid and end).
                start = mid + 1                                                                                            #2. If nums[mid] is greter than target and nums[mid] is before pivot and target is after pivot, target is in the second half(between mid and end).
            else:                                                                                                          #Otherwise, target is in the first half(between start and mid).
                end = mid - 1
        return -1                                                                                                          #If can not find target, return -1.
