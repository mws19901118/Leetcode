class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        prefixSums = [[0] for _ in range(len(piles))]                                                                                                 #Calculate the prefix sums of each pile; prefixSums[i][j] means for pile i, the sum of coin values to take j coins.
        for i, p in enumerate(piles):
            for c in p:
                prefixSums[i].append(prefixSums[i][-1] +c)
        
        @cache                                                                                                                                        #Cache result.
        def dp(pile: int, capacity: int):                                                                                                             #DP to calculate the max value to take capacity coins from in piles[pile:].
            if capacity == 0 or pile == len(piles):                                                                                                   #If capacity is 0 or pile eqauls the length of piles, we reach the end, so return 0.
                return 0
            return max(prefixSums[pile][i] + dp(pile + 1, capacity - i) for i in range(min(capacity + 1, len(prefixSums[pile]))))                     #Then return the max of taking i coins in current pile dp(pile + 1, capacity - 1), i is from 0 to the minimum of capacity and current pile length.
        
        return dp(0, k)                                                                                                                               #Return the result of dp(0, k).
