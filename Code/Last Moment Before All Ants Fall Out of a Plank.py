class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max(0 if not left else max(left), 0 if not right else (n - min(right)))        #Meet doesn't have any actual effect, so it is the max of rightmost in left to left end and leftmost in right to right end.
