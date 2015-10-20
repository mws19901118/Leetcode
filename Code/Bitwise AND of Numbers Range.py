class Solution:
    # @param m, an integer
    # @param n, an integer
    # @return an integer
    def rangeBitwiseAnd(self, m, n):
        mod="0b1"
        l=len(bin(m))-2                   #Calculate the length of binary number of m/
        for i in range(l):                #Calculate the least number which is greater than m and is power of 2.
            mod=mod+'0'
        mod=int(mod,2)
        if n>mod:                         #If n>=mod, the result of AND must be 0.
            return 0
        else:
            result=m
            for i in range(m+1,n+1):      #If n<mod, calculate the result of AND one by one.
                result=result&i
                if result==0:
                    break
            return result
