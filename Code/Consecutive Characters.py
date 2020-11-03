class Solution:
    def maxPower(self, s: str) -> int:
        i, power = 0, 0
        while i < len(s):                           #Use 2 pointers.
            j = i + 1
            while j < len(s) and s[j] == s[i]:
                j += 1
            power = max(power, j - i)               #Find the max length of all consecutive characters substrings.
            i = j
        return power
