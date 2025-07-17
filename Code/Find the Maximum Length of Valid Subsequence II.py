class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0 for _ in range(k)] for _ in range(k)]                #Initialize dp; dp[i][j] means the max length of subsequence with adjacent sum of modulo equals tp j and ending at a number x that x % k == i.
        for x in nums:                                                #Traverse nums.
            y = x % k                                                 #Take modulo.
            for j in range(k):                                        #Traverse k.
                dp[y][j] = max(dp[y][j], dp[(j - y) % k][j] + 1)      #Update dp[y][j] if dp[(j - y) % k][j] + 1 is greater.
        return max(max(r) for r in dp)                                #Return the max in dp.
