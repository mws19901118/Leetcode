class Solution:
    def minChanges(self, s: str) -> int:
        return sum(int(s[i]) ^ int(s[i + 1]) for i in range(0, len(s), 2))    #Make each 2 adjacent characters either all 0 or all 1.
