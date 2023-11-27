class Solution:
    def knightDialer(self, n: int) -> int:
        dp = [1] * 10                                                  #Initialize dp.
        division = 10 ** 9 + 7                                         #Initialize division.
        for _ in range(1, n):                                          #Iterate from 1 to n.
            new_dp = [0] * 10                                          #Initialize new dp.
            new_dp[0] = (dp[4] + dp[6]) % division                     #0 can be reached from 4 and 6.
            new_dp[1] = (dp[6] + dp[8]) % division                     #1 can be reached from 6 and 8.
            new_dp[2] = (dp[7] + dp[9]) % division                     #2 can be reached from 7 and 9.
            new_dp[3] = (dp[4] + dp[8]) % division                     #3 can be reached from 4 and 8.
            new_dp[4] = (dp[0] + dp[3] + dp[9]) % division             #4 can be reached from 0, 3 and 9.
            new_dp[5] = 0                                              #5 cannot be reached from any number.
            new_dp[6] = (dp[0] + dp[1] + dp[7]) % division             #6 can be reached from 0, 1, and 7.
            new_dp[7] = (dp[2] + dp[6]) % division                     #7 can be reached from 2 and 6.
            new_dp[8] = (dp[1] + dp[3]) % division                     #8 can be reached from 1 and 3.
            new_dp[9] = (dp[2] + dp[4]) % division                     #9 can be reached from 2 and 4.
            dp = new_dp                                                #Replace dp with new_dp.
        return sum(dp) % division                                      #Sum up dp and return the mod.
