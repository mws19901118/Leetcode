class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        for c in set(s):                                                                #For each unique characters c in s, if the count of c is smaller than k, split s by c.
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))             #Return the max result of each split.
        return len(s)                                                                   #Otherwise return the length of string.
