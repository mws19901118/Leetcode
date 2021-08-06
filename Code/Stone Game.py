class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = [[0 for _ in range(len(piles))] for _ in range(len(piles))]                                                            #Initialize dp[i][j] to be the max stones one play can take more than the other player in piles[i:j + 1] if starting first.
        for i in range(len(piles)):                                                                                                 #Traverse the span of eahc subarray.
            for j in range(len(piles) - i):                                                                                         #Traverse each subarry whose length is i + 1.
                dp[j][j + i] = piles[j] if i == 0 else max(piles[j] - dp[j + 1][j + i], piles[j + i] - dp[j][j + i - 1])            #If i == 0, dp[j][j + i] = piles[j] since there is only one pile; otherwise, dp[j][j + i] = max(piles[j] - dp[j + 1][j + i], piles[j + i] - dp[j][j + i - 1]), which are result of taking piles[j] and piles[j + i] respectively.
        return dp[0][len(piles) - 1] > 0                                                                                            #If dp[0][len(piles) - 1] > 0, Alex can always win.
    
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True                                                                                                                 #When there are 2 piles: Alex can win obviously by taking the larger pile.
                                                                                                                                    #When there are 4 piles: If Alex takes the first pile initially, she can always take the third pile. If she takes the fourth pile initially, she can always take the second pile. Because total number of stones is odd, at least one of first + third, second + fourth is larger, so she can always win.
                                                                                                                                    #And so on, Alex can always win.
