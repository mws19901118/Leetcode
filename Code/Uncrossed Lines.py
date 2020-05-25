class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp = [[0 for j in range(len(B) + 1)] for i in range(len(A) + 1)]        #dp[i + 1][j + 1] stores the max uncrossed lines between A[:i + 1] and B[:j + 1]
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:                                                #If A[i] == B[j], dp[i + 1][j + 1] = dp[i][j] + 1.
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:                                                           #Otherwise, dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1]).
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[len(A)][len(B)]                                               #Return the final result.
