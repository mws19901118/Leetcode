class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        division = 10 ** 9 + 7                                                                                            #Initialize division.
        @cache                                                                                                            #Cache result.
        def dp(index: int, count: int, currentProfit: int) -> int:
            if index >= len(group):                                                                                       #If current index reaches the end of group, return if current profit is at least minProfit.
                return int(currentProfit >= minProfit)
            schemas = dp(index +1, count, min(currentProfit, minProfit))                                                  #Get the number of schemas skipping current crime, the actual profit does not matter as long as it reaches minProfit.
            if count + group[index] <= n:                                                                                 #If there are enough people, get the number of schemas performing current crime.
                schemas += dp(index + 1, count + group[index], min(currentProfit + profit[index], minProfit))
            return schemas % division                                                                                     #Return the modulo.

        return dp(0, 0, 0)                                                                                                #Return dp(0, 0, 0).
