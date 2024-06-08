class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        return sum(x * (x + 1) // 2 for x in Counter(s).values())        #Count each letter and for each count x, there could be x * (x + 1) // 2 such subarrays.
