class Solution:
    def minEnd(self, n: int, x: int) -> int:
        result = x                                  #Initiailize result to x.
        n -= 1                                      #Decrease n by 1 because the start of array is already x.
        mask = 1                                    #Initialize mask for bit to check.
        while n > 0:                                #Iterate while n > 0.
            if (mask & x) == 0:                     #If the corresponding bit in x is 0, we can set 1 to this bit and create an element that is greater than x and still has same AND with x.
                result |= (n & 1) * mask            #Id the LSB of n is 0, we don't need to do anything; otherwise, add mask to result. This is not the minimum number after (n // 2), but it will end up at the result, as result will increase slow at the beginning and increase fast towards the end; while n is on the contray.
                n >>= 1                             #Shift n right by 1 to process next bit.
            mask <<= 1                              #Shift mask left by 1 for next iteration.
        return result
