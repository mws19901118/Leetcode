class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        division = 10 ** 9 + 7                                                                      #Intialize division.
        l = len(str(k))                                                                             #Get the length of k.
        dp = [1] + [0] * len(s)                                                                     #Initialize dp array, dp[i] means the number of arrays for s[:i], initially, dp[0] is 1.
        for i in range(len(s)):                                                                     #Traverse s.
            if i < len(s) - 1 and s[i + 1] == '0':                                                  #If s[i + 1] is valid and is '0', skip current s[i] because number cannot have leading 0.
                continue
            j = 0
            while i - j >= 0 and j <= l - 1:                                                        #Traverse backward from i.
                if s[i - j] != '0' and (j < l - 1 or int(s[i - j:i + 1]) <= k):                     #If s[i - j] is not '0' and int(s[i - j:i + 1]) is not greater than k, int(s[i - j:i + 1]) is a valid number so add dp[i - j] to dp[i + 1].
                    dp[i + 1] = (dp[i + 1] + dp[i - j]) % division
                j += 1
        return dp[-1]                                                                               #Return dp[-1].
