class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        ways=[1,1]                            #Initialize.
        for i in range(2,n+1):
            ways.append(ways[i-1]+ways[i-2])  #Starting from the second stair, ways[i]=ways[i-1](climb 1 stair)+ways[i-2](climb 2 stairs).
        return ways[n]
