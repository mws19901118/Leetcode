class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        nIsNegative = False
        if n < 0:                                               #If n is negative, let n be its absolute value.
            nIsNegative = True
            n = -n
        value = [x]                                             #value[i]=x^(2^power[i])
        power = [1]
        while power[-1] < n:
            value.append(value[-1]*value[-1])
            power.append(power[-1]*2)
        
        result = 1
        length = len(power) - 1                                 #Record the ending position for binary search.
        while n > 0:
            start = 0
            end = length
            while start < end:                                  #Find the largest power[i] which is smaller than n using binary search.
                mid = (start + end) / 2
                if power[mid] > n:
                    end = mid - 1
                elif power[mid + 1] <= n:
                    start = mid + 1
                else:
                    start = mid
                    break
            n -= power[start]                                   #Update result and n.
            result *= value[start]
            length = start - 1
        if nIsNegative == True:                                 #If n is negative, let result be its reciprocal.
            result= 1 / result
        return result
