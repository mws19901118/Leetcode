class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewel = set([x for x in J])
        count = 0
        for x in S:
            if x in jewel:
                count += 1
        return count
