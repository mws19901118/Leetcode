class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        dp = [0] + [-1] * (len(nums) - 1)                            #Initialize dp, 0 for first number and -1 for the rest.
        for i, x in enumerate(nums):                                 #Traverse nums.
            if dp[i] == -1:                                          #If dp[i] == -1, it is unreachable, so skip.
                continue
            for j, y in enumerate(nums[i + 1:], start = i + 1):      #Traverse nums[i + 1:].
                if -target <= y - x <= target:                       #If j can be reached from i, update dp[j] is dp[i] + 1 is greater.
                    dp[j] = max(dp[j], dp[i] + 1)
        return dp[-1]                                                #Return dp[-1].
