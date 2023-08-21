class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return any(len(s) % i == 0 and s == s[:i] * (len(s) // i) for i in range(1, len(s) // 2 + 1))        #If any i between 1 and len(s) // 2) is a factor of len(s) and s[:i] is a pattern, return true; otherwise, return fales.
