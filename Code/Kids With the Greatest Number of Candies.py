class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)                                         #Find the max candies.
        return [x + extraCandies >= maxCandy for x in candies]          #Return whether current candy plus extra candies will be greater than or equal to max candy for each kid.
