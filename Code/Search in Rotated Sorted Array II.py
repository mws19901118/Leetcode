class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start, end = 0, len(nums) - 1
        while start <= end:                                                 #Binary search.
            mid = (start + end) // 2
            if nums[mid] == target:                                         #If found target, return trie.
                return True
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
            elif nums[mid] > nums[start] and nums[mid] < nums[end]:         #If nums[start] < nums[mid] < nums[end], it's a normal binary search.
                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            else:                                                           #If (nums[mid] >= nums[start] and nums[mid] == nums[end]) or (nums[mid] == nums[start] and nums[mid] <= nums[end]), we cannot determine which half to go.
                if nums[mid] == nums[start]:                                #If nums[start] == nums[mid], increase start; otherwise, decrease end.
                    start += 1
                else:
                    end -= 1
        return False                                                        #If can not find target, return false.
