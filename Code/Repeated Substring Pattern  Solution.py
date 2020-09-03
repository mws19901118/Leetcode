class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return any(s[i] == s[0] and len(s) % i == 0 and all(s[j:j + i] == s[:i] for j in range(i, len(s), i)) for i in range(1, len(s)))    #Traverse string, if s[i] = s[0](i > 0) and len(s) % i == 0, check whether s[:i] is a pattern.
