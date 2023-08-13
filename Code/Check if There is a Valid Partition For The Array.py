class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        @cache                                                                                                                                                                                                           #Cache result.                                                                                 
        def dp(index: int) -> bool:                                                                                                                                                                                      #DP to determine if nums[index:] has a valid partition.
            if index == len(nums):                                                                                                                                                                                       #If index reaches the end of nums, return true.
                return True
            if index < len(nums) - 1 and nums[index] == nums[index + 1] and dp(index + 2):                                                                                                                               #Check for condition 1.
                return True
            if index < len(nums) - 2 and ((nums[index] == nums[index + 1] and nums[index] == nums[index + 2]) or (nums[index] == nums[index + 1] - 1 and nums[index] == nums[index + 2] - 2)) and dp(index + 3):         #Check for condition 2 or 3.
                return True
            return False                                                                                                                                                                                                 #Return false if no condition is satisfied.

        return dp(0)                                                                                                                                                                                                     #Return dp(0).
