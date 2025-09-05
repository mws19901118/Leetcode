class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        k = 1                              #Start from 1.
        while True:                        #Iterate.
            x = num1 - num2 * k            #Deduct num2 k times from num1.
            if x < k:                      #If the x is smaller than k, we can not make x to 0 by duducting a power of 2 from it k times; because the minimum power of 2 is 1.
                return -1                  #Thus return -1.
            if k >= x.bit_count():         #If k is greater than or eqaul to the bits in x, we can make x to 0(2 ** i can be twice of 2 ** (i - 1)), so is it okay if k is greater than the bits in x.
                return k                   #Thus return k.
            k += 1                         #Increase k by 1.
