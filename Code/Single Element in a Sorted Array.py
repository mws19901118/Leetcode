class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:                                                                                           #Binary search in list.
            mid = (start + end) // 2
            if mid == 0 or mid == len(nums) - 1 or (nums[mid - 1] != nums[mid] and nums[mid + 1] != nums[mid]):       #If current number is on either edge of list or both adjacent number is different with current number, return current number. Because it's guranteed there is a unique number, no need to check boundary condition.
                return nums[mid]
            elif (nums[mid - 1] == nums[mid] and mid % 2 == 1) or (nums[mid + 1] == nums[mid] and mid % 2 == 0):      #If current number is not unique and the index of first appearance is even, the unique number is behind current number.
                start = mid + 1
            else:                                                                                                     #Otherwise, the unique number is in front of current number.
                end = mid - 1
