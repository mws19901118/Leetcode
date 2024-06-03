class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0                              #Use 2 pointers to traverse s and t respectively.
        while i < len(s) and j < len(t):
            if s[i] == t[j]:                     #If s[i] == t[j], move forward j.
                j += 1
            i += 1                               #Move forward i.
        return len(t) - j                        #Now, t[:j] is the max subsequence in s, so we only need to append len(t) - j more characters.
