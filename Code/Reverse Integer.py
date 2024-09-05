class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1                            #Get the sign of x.
        x = abs(x)                                            #Take the absolute value of x.
        result = 0                                            #Initialize result.
        while x:                                              #Iterate while x > 0.
            result *= 10                                      #Left shift(as base 10) result a digit.
            result += x % 10                                  #Add the last digit of x to result.
            x //= 10                                          #Right shift(as base 10) x a digit.
        result *= sign                                        #Restore the sign.
        if result < -(2 ** 31) or result > 2 ** 31 - 1:       #Make sure result is valid 32 bits integer, otherwise return 0.
            result = 0
        return result
