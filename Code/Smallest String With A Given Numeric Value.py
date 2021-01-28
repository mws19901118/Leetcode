class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        l = (26 * n - k) // 25            #Try to put as many 'a' in the beginning as possible. (k - l) <= (n - l) * 26.
        s = 'a' * l
        c = k - l - 26 * (n - 1 - l)      #Put next character, and then all 'z'.
        s += chr(ord('a') + c - 1)
        s += 'z' * (n - l - 1)
        return s
