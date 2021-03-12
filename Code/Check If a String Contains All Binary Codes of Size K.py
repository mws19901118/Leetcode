class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        return len({s[i:i + k] for i in range(len(s) - k + 1)}) == 1 << k       #Put all substrings whose length is k in a set and determine if the length of set eqauls 2 ** k.
