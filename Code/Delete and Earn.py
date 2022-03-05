class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)                                       #Count each numbers in nums.
        minV, maxV = min(count.keys()), max(count.keys())           #Get the min value and max value of nums.
        dp = [0] * (maxV + 2)                                       #Initialize dp array from 0 to maxV + 1; dp[i] means the max points earned from 0 minV to i - 1.
        for i in range(minV, maxV + 1):                             #Traverse from minV to maxV.
            dp[i + 1] = max(dp[i], i * count[i] + dp[i - 1])        #If remove i, dp[i + 1] = i * count[i] + dp[i - 1]; otherwise, dp[i + 1] = dp[i], so taking the greater of these 2 values.
        return dp[-1]                                               #Return dp[-1].
