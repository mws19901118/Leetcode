class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        divisor = 10 ** 9 + 7                                                   #Initialize divisor.
        dp = [1] + [0] * (numPeople // 2)                                       #Initialize dp for each 2 * i circle size; dp[0] is 1.
        for i in range(1, numPeople // 2 + 1):                                  #Iterate from 1 to numPeople // 2.
            for j in range(i):                                                  #Traverse from 0 to i - 1, meaning that there is a handshake between person at 0 and person at number 2 * j + 1, then dividing people into 2 sub circles whose sizes are 2 * j and 2 * (i - j - 1) respectively.
                dp[i] = (dp[i] + dp[j] * dp[i - j - 1]) % divisor               #People in sub circles can only hand shake within sub circle. So add dp[j] * dp[i - j - 1] to dp[i] and take modulo by divisor.
        return dp[numPeople // 2]                                               #Return dp[numPeople // 2]; it is also the n-th Catalan number.
