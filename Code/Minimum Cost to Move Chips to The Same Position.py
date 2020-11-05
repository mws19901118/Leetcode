class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        return min(sum(x % 2 == 0 for x in position), sum(x % 2 == 1 for x in position))        #We can move all chips in odd position to the first and all chips in even position to the second without cost. Then just check which is smaller.
