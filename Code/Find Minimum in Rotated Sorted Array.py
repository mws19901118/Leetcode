class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start < end:                                                  #Binary search.
            mid = (start + end) // 2
            if nums[start] <= nums[mid] < nums[end]:                        #If nums[start] <= nums[mid] < nums[end], they are on one side of minimum, return nums[start] because it's the minimum.
                return nums[start]
            if nums[mid] >= nums[start] > nums[end]:                        #If nums[mid] >= nums[start] > nums[end], nums[mid] and nums[start] are on the left side of minimum while nums[end] on the other side, continue binary search in the right half.
                start = mid + 1
            elif nums[start] > nums[end] > nums[mid]:                       #If nums[start] > nums[end] > nums[mid], nums[mid] and nums[end] are on the right side of minimum while nums[start] on the other side.
                if nums[mid - 1] > nums[mid]:                               #If nums[mid - 1] > nums[mid], then nums[mid] is minimum.
                    return nums[mid]
                else:                                                       #Otherwise continue binary search in the left half.
                    end = mid - 1
        return nums[start]
