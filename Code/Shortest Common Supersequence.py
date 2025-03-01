class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)                                                                            #Get the length of str1 and str2.
        dp = [[i if not j else (j if not i else 0) for j in range(n + 1)] for i in range(m + 1)]               #Initialize (m + 1) * (n + 1) dp matrix(dp[i][j] the shortest common supersequence of str1[:i] and str2[:j]): dp[i][0] is i and dp[0][j] is j and the rest of dp are all 0.
        for i, j in product(range(m), range(n)):                                                               #Traverse every character tuples of str1 and str2 from front to behind.
            dp[i + 1][j + 1] = dp[i][j] + 1 if str1[i] == str2[j] else min(dp[i][j + 1], dp[i + 1][j]) + 1     #If str1[i] == str2[j], dp[i + 1][j + 1] is dp[i][j] + 1; otherwise, dp[i + 1][j + 1] is min(dp[i][j + 1], dp[i + 1][j]) + 1.
        x, y = m, n                                                                                            #Initialize x and y to be m and n.
        result = []                                                                                            #Initialize result.
        while x and y:                                                                                         #Iterate while x any are both greater than 0 to restore the shortest common supersequence.
            if str1[x - 1] == str2[y - 1]:                                                                     #If str1[x - 1] == str2[y - 1], append the character to result and move backward both x and y.
                result.append(str1[x - 1])
                x -= 1
                y -= 1
            elif dp[x - 1][y] < dp[x][y - 1]:                                                                  #If dp[x - 1][y] is smaller than dp[x][y - 1], append str1[x - 1] and decrease x.
                result.append(str1[x - 1])
                x -= 1
            else:                                                                                              #Otherwise, append str2[y - 1] and decrease y.
                result.append(str2[y - 1])
                y -= 1
        while x:                                                                                               #While x is greater than 0, append str1[x - 1] and decrease x.
            result.append(str1[x - 1])
            x -= 1
        while y:                                                                                               #While y is greater than 0, append str2[y - 1] and decrease y.
            result.append(str2[y - 1])
            y -= 1
        return "".join(reversed(result))                                                                       #Join the reversed result and return.
