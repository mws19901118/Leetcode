class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):                                                                                                                              #If s1 and s2 aren't same length, return false.
            return False
        misMatches = [i for i in range(len(s1)) if s1[i] != s2[i]]                                                                                          #Find all the indexes that are mismatch between s1 and s2.
        return not misMatches or (len(misMatches) == 2 and s1[misMatches[0]] == s2[misMatches[1]] and s1[misMatches[1]] == s2[misMatches[0]])               #If should be either no mismatches or exactly 2 mismatches and corresponding characters equal after swap.
