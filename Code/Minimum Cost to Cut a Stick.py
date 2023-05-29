class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + sorted(cuts) + [n]                                                                                                   #Sort cuts(because we can change order) and add 2 dummy cut on both ends(0 at start and n at end).
        @cache                                                                                                                            #Cache result.
        def dp(start: int, end: int) -> int:                                                                                              #Calculate the cost to cut cuts[start:end + 1], which are uncut yet.
            if start > end:                                                                                                               #If start > end, there is no need to cut, return 0.
                return 0
            return cuts[end + 1] - cuts[start - 1] + min([dp(start, i - 1) + dp(i + 1, end) for i in range(start, end + 1)])              #For either cut in cuts[start:end + 1], the cost is cuts[end + 1] - cuts[start - 1].
                                                                                                                                          #So, traverse each cut in cuts[start:end + 1], calculate the cost of further cutting recursively and then add the cost to cut itself then return.
        return dp(1, len(cuts) - 2)                                                                                                       #Return the dp result of 1 and len(cuts) - 2.
