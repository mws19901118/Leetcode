class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        if len(S)==0 or len(T)==0:
            return 0
        dp=[0]*len(T)
        for i in range(len(S)):
            for j in range(len(T)):
                if S[len(S)-1-i]==T[j]:
                    if j==len(T)-1:
                        dp[j]+=1
                    else:
                        dp[j]+=dp[j+1]
        return dp[0]
        
  #Basically the idea is iterate from the end of S, and if SS[len(S)-1-i]==T[j], 
  #then the distinct sub sequences of T.substring(j) in S.substring(i) can be calculated as dp[j]=dp[j]+dp[j+1]. 
  #The final result is occu[0]. 
