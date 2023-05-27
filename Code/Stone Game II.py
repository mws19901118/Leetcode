class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @cache                                                                              #Cache result.
        def dp(index: int, m: int, isAlice: bool):                                          #Use dp to calculate the max stones Alice can get for piles[index + 1:] and m and if the player is Alice.
            if index >= len(piles) - 1:                                                     #If index >= len(piles) - 1, it reaches the end, so return 0.
                return 0
            result = 0 if isAlice else float('inf')                                         #Initialize result, if player is alice, we will return current max value; otherwise, return current min value.
            s = 0                                                                           #Initialize the sum of stones Alice takes in this turn.
            for x in range(1, min(2 * m + 1, len(piles) - index)):                          #Traverse from 1 to min(2 * m, len(piles) - index - 1).
                s += piles[index + x]                                                       #Take current pile.
                if isAlice:                                                                 #If player is Alice, calculate the result of stop now and let Bob play, then update result if necessary.
                    result = max(result, s + dp(index + x, max(m, x), False))
                else:                                                                       #Otherwise, calculate the result of stop now and let Alice play, then update result if necessary.
                    result = min(result, dp(index + x, max(m, x), True))
            return result                                                                   #Return result.
        return dp(-1, 1, True)                                                              #Start dp when index is -1 and m is 1 and player is Alice.
