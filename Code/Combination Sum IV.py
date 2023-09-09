class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache                                                             #Cache result.
        def dp(target: int) -> int:                                        #DP to find number of combinations for given target.
            if not target:                                                 #If target is 0, return 1.
                return 1
            return sum(dp(target - x) for x in nums if x <= target)        #For all numbres in nums that are not greater than target, there are dp(target - x) ways to form given target with x.

        return dp(target)                                                  #Return dp(target).
