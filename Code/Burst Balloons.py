class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0, 1)                                                   #Add the unreal nums[-1] in the beginning of nums.
        nums.append(1)                                                      #Add the unreal nums[n] in the end of nums.
        dp = [[0 for j in range(len(nums))] for i in range(len(nums))]      #Record the max sum of coins collected from nums[i] to nums[j](consider nums[i] and nums[j] unreal).
        for i in range(2, len(nums)):                                       #Examine every length of intevals from i to j; the minimum length is 2.
            for j in range(0, len(nums) - i):                               #Examine every intevals of current length.
                for k in range(j + 1, j + i):                               #Check every possible balloon as the last one to burst. That means divide the intevals into to subintevals at the last bolloon to burst and calculate which partition will make the most coins.
                    dp[j][j + i] = max(dp[j][j + i], nums[j] * nums[k] * nums[j + i] + dp[j][k] + dp[k][j + i])
        return dp[0][len(nums) - 1]                                                    #Return the coins collected from nums[-1] to nums[n].
