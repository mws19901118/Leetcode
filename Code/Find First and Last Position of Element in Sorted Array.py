class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = []
        start, end = 0, len(nums) - 1
        while start <= end:                                                                   #Binary search for the first position.
            mid = (start + end) // 2
            if nums[mid] == target and (mid - 1 < 0 or nums[mid - 1] < target):
                result.append(mid)
                break
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        start, end = 0, len(nums) - 1
        while start <= end:                                                                   #Binary search for the last position.
            mid = (start + end) // 2
            if nums[mid] == target and (mid + 1 >= len(nums) or nums[mid + 1] > target):
                result.append(mid)
                break
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return result if result else [-1, -1]                                                 #Return result if found first and last position; otherwise, return [-1, -1].
