class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start < end:                                                   #Do binary search from 0 to len(nums) - 1.
            mid = (start + end) // 2
            if nums[mid] > nums[mid + 1]:                                    #If nums[mid] > nums[mid + 1], potential peak is in nums[:mid + 1].
                end = mid
            else:                                                            #Otherwise potential peak is in nums[mid + 1:].
                start = mid + 1
        return start                                                         #Return start after binary search.
