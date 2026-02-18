class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        lastDigit = n & 1                  #Get the last digit of n.
        while n:                           #Iterate while n > 0.
            n >>= 1                        #Right shift n 1 bit.
            if not (n & 1) ^ lastDigit:    #If the current last digit is same with previous last digit, return false.
                return False
            lastDigit = n & 1              #Replace lastDigit with current last digit.
        return True                        #Return true at the end.
