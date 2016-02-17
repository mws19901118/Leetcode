class Solution:
    # @return an integer as the maximum profit 
    def maxProfit(self, k, prices):
        res=0
        n=len(prices)
        if n==0:
            return 0
        peak=[]                                                                     #Record peak and nadir elements, including the start and the end.
        for i in range(1,n):
            if prices[i]>prices[i-1]:
                res+=prices[i]-prices[i-1]                                          #Calculate the total profit without restriction.
        peak.append(prices[0])
        for i in range(1,n-1):
            if (prices[i-1]<=prices[i] and prices[i+1]<prices[i]) or (prices[i-1]>=prices[i] and prices[i+1]>prices[i]):
                peak.append(prices[i])
        if n>1:
            peak.append(prices[-1])
            
        l=len(peak)
        if k>=l/2:                                                                  #If k is greater than the half length of peak, then we can do transaction whenever we want, return the total profit without restriction.
            return res
        dp=[[0 for i in range(l+1)] for j in range(k)]                              #Use dp[k][i+1] represents the max profit of using [0,i] data(only consider peak elements) and k transactions.
        for i in range(1,k+1):                                                      #dp[k][i+1]=max(dp[k-1][i+1], dp[k][i], peak[i] + max( dp[k-1][j] - peak[j] )) { 0 <= j < i }
            currentmax=-0xFFFFFFFF
            for j in range(l):
                dp[i%2][j+1]=max(dp[(i-1)%2][j+1],dp[i%2][j],peak[j]+currentmax)    
                currentmax=max(currentmax,dp[(i-1)%2][j]-peak[j])
        return dp[k%2][l]
