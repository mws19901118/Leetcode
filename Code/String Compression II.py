class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache                                                                            #Cache result.
        def dp(i, k, prev, count):                                                        #Find the min length for s[:i + 1] with k characters left to delete with prev as the previous character on the right and count as it's count.
            if i < 0:                                                                     #If i < 0, dp reaches the beginning of s, return 0.
                return 0
                                                                                          #Case 1: not deleting current character.
            if prev is None or prev != s[i]:                                              #If no previous character or previous character is not current character, set result to 1 + dp(i - 1, k, s[i], 1), because we will have at least 1 length for current character.
                result = 1 + dp(i - 1, k, s[i], 1)
            elif prev == s[i]:                                                            #If previous character is same as current character, set result to (count in [1, 9, 99]) + dp(i - 1, k, s[i], count + 1), because if count is 1, 9 or 99, the length will increase by 1.
                result = (count in [1, 9, 99]) + dp(i - 1, k, s[i], count + 1)
                                                                                          #Case 2: deleting current character.
            if k > 0:                                                                     #if we can delete current character, delete it and update result if dp(i - 1, k - 1, prev, count) is smaller than result. Decrease k and keep prev and count.
                result = min(result, dp(i - 1, k - 1, prev, count))
                
            return result                                                                 #Return result.
      
        return dp(len(s) - 1, k, None, 0)                                                 #Return dp(len(s) - 1, k, None, 0).
