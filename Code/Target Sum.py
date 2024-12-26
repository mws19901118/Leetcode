class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache                                                                                    #Cache result.
        def dp(index: int, remain: int) -> int:                                                   #DP to calculate the ways to make remain using nums[index:].
            if index == len(nums):                                                                #If reaches the end, return 1 if remain is 0 or 0 if not.
                return int(not remain)
            return dp(index + 1, remain + nums[index]) + dp(index + 1, remain - nums[index])      #Return the sum of dp(index + 1, remain + nums[index])(put '-' in front of nums[index]) and dp(index + 1, remain - nums[index])(put '+' in front of nums[index]).
        return dp(0, target)                                                                      #Return dp(0, target).
