class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        divisor = 10 ** 9 + 7                                                                               #Initialize divisor.
        dp = [1] + [0] * target                                                                             #Initialize dp array for the possible ways of summing from 0 to target. For 0 it's 1; for other values it's 0.
        for i in range(n):                                                                                  #Iterate n times to simulate rolling dice n times.
            newdp = [0] * (target + 1)                                                                      #Initialize the newdp for current iteration.
            for j in range(i + 1, min(target, n * k) + 1):                                                  #Traverse from i + 1 to min(target, n * k).
                newdp[j] = (newdp[j - 1] + dp[j - 1] - (dp[j - 1 - k] if j > k else 0)) % divisor           #Calculate newdp[j]. Since, for any j, newdp[j] = sum from dp[max(0, j - k)] to dp[j - 1]. Then for newdp[j + 1], it's from dp[max(0, j + 1 - k)] to dp[j]. Then newdp[j + 1] = newdp[j] + dp[j] - (dp[j - k] if j > k else 0). Calculate the result then module by divisor.
            dp = newdp                                                                                      #Replace dp with newdp.
        return dp[-1]                                                                                       #Return dp[-1].
