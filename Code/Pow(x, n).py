class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        nIsNegative=False
        if n<0:                                           #If n is negative, let n be its absolute value.
            nIsNegative=True
            n=-n
        value=[x]                                         #value[i]=x^(2^power[i])
        power=[1]
        while power[-1]<=n/2:
            value.append(value[-1]*value[-1])
            power.append(power[-1]*2)
        
        result=1
        l=len(power)-1
        while n>0:
            while power[l]>n:                             #Find the largest power[i] which is smaller than n.
                l-=1
            result*=value[l]                              #Update result and n.
            n-=power[l]
        
        if nIsNegative==True:                             #If n is negative, let result be its reciprocal.
            result=1/result
        return result
