class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        dp, prev = [], []                                                                                                              #Initialize dp as the max legit subsequence length ending at each idnex and prev as the previous index of the subsequence.
        max_length, end = 0, -1                                                                                                        #Initialize the max subsequence length and its ending index.
        for i, x in enumerate(words):                                                                                                  #Traverse words.
            dp.append(1)                                                                                                               #Append 1 to dp as a new subsequence only contains current index.
            prev.append(-1)                                                                                                            #Append -1 to prev because no prev index.
            for j, y in enumerate(words[:i]):                                                                                          #Traverse words[:i].
                if groups[i] != groups[j] and len(x) == len(y) and sum(u != v for u, v in zip(x, y)) == 1 and dp[j] + 1 > dp[i]:       #For index i and j, if their groups are unequal and words have same length with hamming distance equals 1, i can be add to the subsequence ending at j.
                    dp[i] = dp[j] + 1                                                                                                  #Update dp[i] if that creates a longer subsequence than current dp[i].
                    prev[i] = j                                                                                                        #Also set prev[i] to j.
            if dp[i] > max_length:                                                                                                     #If final dp[i] is greater than max length, update max length and end.
                max_length = dp[i]
                end = i
        result = []                                                                                                                    #Initialize result.
        while end != -1:                                                                                                               #Trace back until end is -1.
            result.append(words[end])                                                                                                  #Append words[end] to result.
            end = prev[end]                                                                                                            #Set end to prev[end].
        return result[::-1]                                                                                                            #Reverse result and return.
