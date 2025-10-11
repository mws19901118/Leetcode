class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        count = Counter(power)                                                           #Count each power.
        spells = sorted(list(count.keys()))                                              #Sort unique power values in ascending order.
        @cache                                                                           #Cache result.
        def dp(index: int) -> int:                                                       #DP to calculate the max damage using spells in dp[index:].
            if index == len(spells):                                                     #Return 0 if index reaches the end.
                return 0
            i = index + 1                                                                #Find the smallest index i such that i is invalid or spells[i] > spells[index] + 2.
            while i < len(spells) and spells[i] <= spells[index] + 2:
                i += 1
            return max(dp(index + 1), spells[index] * count[spells[index]] + dp(i))      #Calculate the max damage of picking dp[index](spells[index] * count[spells[index]] + dp(i)) and not picking dp[index](dp(index + 1)), return the max of 2.
        return dp(0)                                                                     #Return dp(0).
