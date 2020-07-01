class Solution:
    def arrangeCoins(self, n: int) -> int:                                  #x * (x + 1) // 2 + k = n, 0 <= k <= x + 1.
        return (int)(sqrt(2 * n + 0.25) - 0.5)                              #(x + 0.5) ^ 2 - 0.25 + k = n.
                                                                            #x = int(sqrt(2 * n + 0.25) - 0.5)
