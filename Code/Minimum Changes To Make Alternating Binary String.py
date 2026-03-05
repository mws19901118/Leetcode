class Solution:
    def minOperations(self, s: str) -> int:
        return min(sum(int(x) ^ b ^ (i & 1) for i, x in enumerate(s)) for b in [0, 1])    #Try both starting with 0 and 1 then take the smaller result.
