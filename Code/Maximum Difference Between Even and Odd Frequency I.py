class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)                                                                                        #Count each character in s.
        return max([x for x in count.values() if x & 1]) - min([x for x in count.values() if not x & 1])          #Find the max of odd count and min of even count then calculate the max diff.
