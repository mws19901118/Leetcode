class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m, n = len(strs), len(strs[0])                                   #Get the dimensions.
        dp = [1] * n                                                     #Initialize dp for max whole column increasing subsequence ending at each index.
        for i in range(n):                                               #Traverse each index.
            for j in range(i):                                           #Traverse each index smaller than i.
                if all(strs[k][j] <= strs[k][i] for k in range(m)):      #If for every row letter on column j is not greater than letter on column i, append column i after the whole column increasing subsequence ending at column j to form a new whole column increasing subsequence.
                    dp[i] = max(dp[i], dp[j] + 1)
        return n - max(dp)                                               #Keep the max whole column increasing subsequence then delete the rest columns.
