class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [0] * (len(word2) + 1)
        for i, x in enumerate(word1):                                                                                     #Calculate the length of longest common subsequence of word1 and word2 using dynamic programming.
            previousDPJ = dp[0]
            for j, y in enumerate(word2):
                previousDPJ, dp[j + 1] = dp[j + 1], previousDPJ + 1 if x == y else max(previousDPJ, dp[j], dp[j + 1])     #Use previousDPJ to store the dp[j] value in last iteration and keep update it.
        return len(word1) + len(word2) - 2 * dp[-1]                                                                       #Return the sum of word1 length and word2 length minus twices of length of longest common subsequence.
