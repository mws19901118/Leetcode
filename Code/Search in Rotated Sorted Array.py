class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[start] and nums[mid] > nums[end]:          #If nums[mid] >= nums[start] and nums[mid] > nums[end], the rotate pivot is the right side of mid.
                if nums[mid] > target and target >= nums[start]:            #If nums[start] <= target < nums[mid], target is in the left side of mid; otherwise, target is in the right side of mid.
                    end = mid - 1
                else:
                    start = mid + 1
            elif nums[mid] < nums[start] and nums[mid] <= nums[end]:        #If nums[mid] < nums[start] and nums[mid] <= nums[end], the rotate pivot is the left side of mid.
                if nums[mid] < target and target <= nums[end]:              #If nums[mid] < target <= nums[end], target is in the right side of mid; otherwise, target is in the left side of mid.
                    start = mid + 1
                else:
                    end = mid - 1
            elif nums[mid] >= nums[start] and nums[mid] <= nums[end]:       #If nums[start] <= nums[mid] <= nums[end], it's a normal binary search.
                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1                                                           #If can not find target, return -1.
