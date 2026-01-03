class Solution:
    def numOfWays(self, n: int) -> int:
        division = 10 ** 9 + 7                                                            #Initialize division.
        def dp(x: int) -> (int, int):                                                     #DP function to calculate the ways ending at ABA pattern and ABC pattern for x.
            if x == 1:                                                                    #If x == 1, both ABA and ABC pattern equals 6.
                return 6, 6
            aba, abc = dp(x - 1)                                                          #Get the ABA pattern and ABC pattern for x - 1.
            return (aba * 3 + abc * 2) % division, (aba * 2 + abc * 2) % division         #ABA pattern can be transited to (BAB, BAC, BCB, CAB, CAC) and ABC pattern can be transited to (BAB, BCB, BCA, CAC).
                                                                                          #Thus, new ABA pattern is (aba * 3 + abc * 2) % division and new ABC pattern is (aba * 2 + abc * 2) % division.
        aba, abc = dp(n)                                                                  #Get the ABA pattern and ABC pattern for n.
        return (aba + abc) % division                                                     #Return the sum of ABA pattern and ABC pattern after taking modulo.
