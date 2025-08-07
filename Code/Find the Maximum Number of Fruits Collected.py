class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)                                                                    #Get the dimension.
        diagonal = 0                                                                       #Initialize the sum of the diagonal.
        for i in range(n):                                                                 #Traverse the diagonal to calculate the sum.
            diagonal += fruits[i][i]
            fruits[i][i] = 0                                                               #Also reset all fruits on the diagonal to 0.

        @cache                                                                             #Cache result.
        def dp1(x: int, y: int) -> int:                                                    #DP to calculate the max fruit collected by the child starting at the top right corner.
            if n - 1 - y >= n - 1 - x or y >= n:                                           #It cannot across the diagonal because then it cannot reach the destination. It should also not touch diagonal because all fruits on the diagonal is already taken. Then it obviously cannot step out of bound.
                return -inf                                                                #In any of above case, return negative infinity.
            return fruits[x][y] + max(0, max(dp1(x + 1, z) for z in [y - 1, y, y + 1]))    #For current coordinate, the max is current fruit plus the max from next 3 options(0 if none is valid).

        @cache                                                                             #Cache result.
        def dp2(x: int, y: int) -> int:                                                    #DP to calculate the max fruit collected by the child starting at the bottom left corner.
            if n - 1 - x >= n - 1 - y or x >= n:                                           #It cannot across the diagonal because then it cannot reach the destination. It should also not touch diagonal because all fruits on the diagonal is already taken. Then it obviously cannot step out of bound.
                return -inf                                                                #In any of above case, return negative infinity.
            return fruits[x][y] + max(0, max(dp2(z, y + 1) for z in [x - 1, x, x + 1]))    #For current coordinate, the max is current fruit plus the max from next 3 options(0 if none is valid).

        return diagonal + dp1(0, n - 1) + dp2(n - 1, 0)                                    #Return the sum of diagonal, dp1(0, n - 1), dp2(n - 1, 0).
