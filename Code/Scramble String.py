class Solution:
    @cache                                                                                                                                                                                                       #Cache result.
    def isScramble(self, s1: str, s2: str) -> bool:
        return s1 == s2 or any((self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])) for i in range(1, len(s1)))      #For s2 to be scramble of s1, either s1 == s2, or there exist an index i so that s2[:i] is scramble of s1[:i] and s2[i:] is scramble of s1[i:] or there exist an index i so that s2[-i:] is scramble of s1[:i] and s2[:-i] is scramble of s1[i:].
    
