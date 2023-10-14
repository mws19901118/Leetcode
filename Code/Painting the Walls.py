class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        @cache                                                                              #Cache result.
        def dp(i: int, remain: int) -> int:                                                 #Use dp to calculate the min cost of painting remain walls when considering index i and beyond.
            if remain <= 0:                                                                 #If remain is not positive, return 0 as no more walls need to be painted.
                return 0
            if i == len(cost):                                                              #If i reaches the end of walls while remain is still positive, return inf as it is impossible to finish.
                return inf

            return min(cost[i] + dp(i + 1, remain - 1 - time[i]), dp(i + 1, remain))        #Return the min value of ues paid painter here then use free painter time[i] times(cost[i] + dp(i + 1, remain - 1 - time[i])) or not use free painter(dp(i + 1, remain)).
    
        return dp(0, len(cost))                                                             #Return dp(0, len(cost)).
