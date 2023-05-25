class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if not k:                                 #If k is 0, return 1 directly because no draw needed and current point 0 is always smaller than n.
            return 1
        dp = [1] + [0] * n                        #Store the probability of reaching each point; initially dp[0] is 1 while the rest are 0.
        s = 1                                     #Initialize the probability that will contribute to current probability.
        for i in range(1, n + 1):                 #Traverse from 1 to n.
            dp[i] = s / maxPts                    #Since a draw will add point uniformly, dp[i] = s / maxPts.
            if i < k:                             #If i < k, dp[i] will contribute to future points, so add dp[i] to s.
                s += dp[i]
            if maxPts <= i < k + maxPts:          #If maxPts <= i < k + maxPts, dp[i - maxPts] either doesn't exist or won't contribute to future points, so substract dp[i - maxPts] from s.
                s -= dp[i - maxPts]
        return sum(dp[k:])                        #Return sum(dp[k:]) as the sum of probability from k to n.
