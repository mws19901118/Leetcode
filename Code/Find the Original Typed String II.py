class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        division = 10 ** 9 + 7                                                  #Initialize division.
        chunks = []                                                             #Store the length of every chunk of consecutive characters.
        i = 0
        while i < len(word):                                                    #Populate chunks.
            j = i
            while j < len(word) and word[i] == word[j]:
                j += 1
            chunks.append(j - i)
            i = j

        result = 1                                                              #Calculate the result of total possible original strings(no limitation on string length).
        for x in chunks:
            result = result * x % division

        if len(chunks) >= k:                                                    #If there are at least k chunks, then any orignial string will have at least k characters, so directly return result.
            return result

        dp = [0] * k                                                            #Initialize dp, dp[i] means the count of orignial strings that have i characters.
        prefix_sum = [1] * k                                                    #Store the prefix sum from dp[0] to dp[i] in prefix_sum[i], which is also the count of orignial strings that have at most i characters.
        for i, x in enumerate(chunks):                                          #Traverse chunks.
            for j in range(1, k):                                               #Traverse from 1 to k - 1.
                dp[j] = prefix_sum[j - 1]                                       #Initialize current dp[j] is with the sum of previous prefix_sum[j - 1]. Basically, for each orignial string that have at most j - 1 characters with first i chunks, append some characters of the i + 1 chunk to make an original string that have j characters.
                if j - 1 - x >= 0:                                              #However, the i + 1 chunk may not have enough characters if j - 1 - x >= 0.
                    dp[j] = (dp[j] - prefix_sum[j - 1 - x]) % division          #Thus, we have to deduct prefix_sum[j - 1 - x] from dp[j].
            prefix_sum[0] = dp[0]                                               #Update prefix_sum to reflect the prefix sum of current dp list.
            for j in range(1, k):
                prefix_sum[j] = (prefix_sum[j - 1] + dp[j]) % division
        return (result - prefix_sum[-1]) % division                             #Deduct prefix_sum[-1] from result, which means the count of original strings that have at least k characters. Take modulo then return.
