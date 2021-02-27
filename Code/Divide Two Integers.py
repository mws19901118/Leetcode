class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        flag = (dividend < 0) ^ (divisor < 0)                               #Get the sign of quotient.
        dividend, divisor = abs(dividend), abs(divisor)                     #Get the absolute value of dividend and divisor.
        if dividend < divisor:                                              #If dividend < divisor, return 0.
            return 0
        quotient = 1                                                        #Initalize quotient to be 1.
        x = divisor                                                         #Set x to divisor.
        while dividend >= x << 1:                                           #While dividend is larger than or equal to 2 * x, double x and double quotient.
            x <<= 1
            quotient <<= 1
        quotient += self.divide(dividend - x, divisor)                      #Till now, we have find the max k such that dividend = 2 ** k * divisor + remain. Calculate the quotient of remain / divisor and add it to current quotient, i.e 2 ** k.
        quotient = -quotient if flag else quotient                          #Restore the sign.
        quotient = 2 ** 31 - 1 if quotient > 2 ** 31 - 1 else quotient      #Handle overflow.
        return quotient
