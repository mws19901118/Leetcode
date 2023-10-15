class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        division = 10 ** 9 + 7                                                                                  #Initialize division.
        @cache                                                                                                  #Cache result.
        def dp(n: int, position: int) -> int:                                                                   #DP to find the number of ways to stay at position after n steps.
            if position < 0 or position >= arrLen or position > n:                                              #If position is out of arrLen bound or is greter than n, it is invalid or unreachable, so return 0.
                return 0
            if not n:                                                                                           #If n is 0, return 1.
                return 1
            return (dp(n - 1, position) + dp(n - 1, position - 1) + dp(n - 1, position + 1)) % division         #Return the sum of stay(dp(n - 1, position)), move from left(dp(n - 1, positiion - 1)) and move from right(dp(n - 1, position + 1)) then take modulo.
        
        return dp(steps, 0)                                                                                     #Return do(steps, 0).
