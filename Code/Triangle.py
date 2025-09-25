class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[0]                                                                                                     #Store the minimum path sum at current row, initially it's the first row of triangle.
        for r in triangle[1:]:                                                                                               #Traverse triangle by level starting from 2nd level.
            dp = [dp[0] + r[0]] + [r[i] + min(dp[i - 1], dp[i]) for i in range(1, len(r) - 1)] + [dp[-1] + r[-1]]            #Calculate the minimal path sum at current level and updae dp.
        return min(dp)                                                                                                       #Return minimum number in dp.
