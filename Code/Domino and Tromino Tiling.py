class Solution:
    def numTilings(self, n: int) -> int:
        if n < 3:                                                     #If n < 3, return n as there is one length 1 tiling and two length 2 tilings.
            return n
        division = 10 ** 9 + 7                                        #Division is 10 ** 9 + 7.
        dp1, dp2, dp3 = 1, 1, 2                                       #Initialize DP value for the last 3 elements; inititally for n = 0, 1, 2.
        for i in range(2, n):                                         #Compute the DP value, from 3 to n; suppose the DP function is F(), then the dp value is F(x).
            dp1, dp2, dp3 = dp2, dp3, (dp3 * 2 + dp1) % division)     #For any x >= 3. Tiling can be formed by add a vertical domino to each of length x - 1 tiling, or add 2 horizontal dominos to each of length x - 2 tiling.
        return dp3                                                    #We can also use 2 trominos at both end and any number of dominos(including 0) in the middle to form tiling whose length is longer than or equal to 3.
                                                                      #Below are examples, '-' as domino and '*' as tromino.
                                                                      #length of 3:
                                                                      #  * * *
                                                                      #  * * *
                                                                      #length of 4:
                                                                      #  * * * *
                                                                      #  * - - *
                                                                      #length of 5:
                                                                      #  * * - - *
                                                                      #  * - - * *
                                                                      #length of 6:
                                                                      #  * * - - * *
                                                                      #  * - - - - *
                                                                      #and so on and so forth...
                                                                      #Because trominos can be flip up and down to make different tilling, we can form 2 new tilings for each of length i tiling, 0 <= i <= x - 3.
                                                                      #Thus, F(x) = F(x - 1) + F(x - 2) + (F(0) + ... + F(x - 3)) * 2.
                                                                      #In same way, F(x + 1) = F(x) + F(x - 1) + (F(0) + ... + F(x - 2)) * 2 = F(x) + (F(x - 1) + F(x - 2) + (F(0) + ... + F(x - 3)) * 2) + F(x - 2) = F(x) * 2 + F(x - 2).
                                                                      #So, the state transition equation is F(n) = F(n - 1) * 2 + F(n - 3) for n >= 3.
                                                                      #Compute the DP value and get the modulo.
                                                                      #Return dp3.
