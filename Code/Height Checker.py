class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortedHeights = sorted(heights)                                        #Sort heights.
        return sum(1 for x, y in zip(heights, sortedHeights) if x != y)        #Return the count of positions where the height and sortedHeight mismatch.
