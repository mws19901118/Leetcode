class Solution:
    def titleToNumber(self, s: str) -> int:
        return sum([(ord(s[i]) - ord('A') + 1) * pow(26, len(s) - 1 - i) for i in range(len(s))])     #Convert base 26 string to int.
