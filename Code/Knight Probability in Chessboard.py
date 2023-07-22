class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        @cache                                                                                                                                                                                          #Cache result.
        def dp(x: int, y: int, move: int) -> float:                                                                                                                                                     #Calculate the probability of remains on the board at x, y with remain moves.
            if x < 0 or x >= n or y < 0 or y >= n:                                                                                                                                                      #If x or y is out of board boundary, return 0.
                return 0
            if not move:                                                                                                                                                                                #If no more moves, return 1.
                return 1
            return sum(dp(u, v, move - 1) for u, v in [(x - 2, y + 1), (x - 1, y + 2), (x + 1, y + 2), (x + 2, y + 1), (x + 2, y - 1), (x + 1, y - 2), (x - 1, y - 2), (x - 2, y - 1)]) / 8             #Return the sum of dp result in 8 directions with one fewer move divided it by 8.

        return dp(row, column, k)                                                                                                                                                                       #Return the dp result from the starting point.
