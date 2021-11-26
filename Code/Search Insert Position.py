class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:                                                       #If target > nums[-1], insert target at the end of nums.
            return len(nums)
        start, end = 0, len(nums) - 1
        while start <= end:                                                         #Binary search.
            mid = (start + end) // 2
            if (mid == 0 or nums[mid - 1] < target) and nums[mid] >= target:        #If (mid == 0 or nums[mid - 1] < target) and nums[mid] >= target, insert target at mid.
                return mid
            elif nums[mid] < target:                                                #Else, if nums[mid] < target, search target in nums[mid + 1:end + 1].
                start = mid + 1
            else:                                                                   #Otherwise, search target in nums[start:mid].
                end = mid - 1
