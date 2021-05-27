class Solution:
    def minPartitions(self, n: str) -> int:
        return max(int(x) for x in n)         #Because deci-binary is only 0 or 1, so there won't be carry. Just return the largest digit.
