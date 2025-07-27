class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        i, count = 0, 0                                                                                #Initialize i to traverse nums and count.
        while i < len(nums):                                                                           #Traverse nums with 2 pointers.
            j = i
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            if i - 1 >= 0 and j < len(nums) and (nums[i - 1] - nums[i]) * (nums[j] - nums[i]) > 0:     #If both non-equal neighbors exist and are either greater or smaller than current number at same time, current number is in a hill or valley.
                count += 1
            i = j
        return count
