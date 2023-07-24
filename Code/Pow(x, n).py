class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:                        #If n < 0, set n to its absolute value and set x to its reciprocal.
            n = -n
            x = 1 / x
        power = 1                        #Initialize power to be 1.
        while n:                         #Iterate while n is larger than 0.
            if n & 1:                    #If last digit of n is 1, multiple power by x.
                power *= x
            n >>= 1                      #Right shift n 1 bit.
            x **= 2                      #Replace x with its square.
        return power                     #Return power.
