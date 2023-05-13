class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        division = 10 ** 9 + 7                      #Initialize division.
        dp = [1] + [0] * high                       #Initialize dp array with dp[0] = 1 and others are 0.
        for i in range(1, high + 1):                #Traverse from 1 to high.
            if i - zero >= 0:                       #If i - zero >= 0, add dp[i - zero] to dp[i].
                dp[i] += dp[i - zero]
            if i - one >= 0:                        #If i - one >= 0, add dp[i - one] to dp[i].
                dp[i] += dp[i - one]
            dp[i] %= division                       #Take the mod.
        return sum(dp[low:]) % division             #Sum up dp[low:] and take the mod and return.
