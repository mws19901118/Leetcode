class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(map(lambda s: s in set(J), S))
