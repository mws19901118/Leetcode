class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = Counter()                                                         #Count the frequency of each character in window.
        start, max_frequency = 0, 0                                               #Initialize the left bound of window and the max frequency in the window.
        result = 0                                                                #Initialize result.
        for end in range(len(s)):                                                 #Traverse all right bound of window.
            count[s[end]] += 1                                                    #Increase frequency of s[end].
            max_frequency = max(max_frequency, count[s[end]])                     #Update max frequency.
            if end - start + 1 - max_frequency > k:                               #If the window length minus max frequency is larger than k, we cannot replace k characters to make window valid.
                count[s[start]] -= 1                                              #Decrease the frequency of s[start] and move forward start.
                start += 1                                                        #After move, the window might not be valid, but since we have already seen a valid window with same size, it does not affect the result, so we don't need to move start further forward and shrink window size. 
            result = max(result, end - start + 1)                                 #Update result.
        return result
