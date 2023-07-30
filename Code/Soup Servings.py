class Solution:
    def soupServings(self, n: int) -> float:
        m = ceil(n / 25)                                                                                                            #Since the minimum serving size is 25ml and is based on best efforts, convert n to serving size by taking ceil(n / 25).
        @cache                                                                                                                      #Cache result.
        def dp(a: int, b: int) -> float:                                                                                            #DP to find the probability result when given a ml of A and b ml of B.
            if not a and not b:                                                                                                     #If a and b are both 0, return 0.5.
                return 0.5
            elif not a and b:                                                                                                       #If only a is 0, return 1.0.
                return 1.0
            elif a and not b:                                                                                                       #If only b is 0, return 0.0.
                return 0.0
            else:                                                                                                                   #Otherwise, return the sum of probability of serving all 4 types then divide by 4.
                return sum(dp(max(0, a + x), max(0, b + y)) for x, y in [(-4, 0), (-3, -1), (-2, -2), (-1, -3)]) / 4
        
        for i in range(1, m + 1, 10):                                                                                               #Serving types are not symmetric, so as m is increasing, the probability is closer to 1. 
            if dp(i, i) > 1.0 - 0.1 ** 5:                                                                                           #Since the precision is 10 ** -5, spot check from 1 to m, if the result is close enough to 1.0, return 1.0 directly.
                return 1.0
        return dp(m, m)                                                                                                             #Return dp(m, m).
