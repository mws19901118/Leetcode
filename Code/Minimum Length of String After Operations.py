class Solution:
    def minimumLength(self, s: str) -> int:
        return sum((x + 1) % 2 + 1 for x in Counter(s).values())    #Count each character in s, and for each count x, reduce it by 2 until smaller than 3, which is equivlant to (x + 1) % 2 + 1. SUm up the result and return.
