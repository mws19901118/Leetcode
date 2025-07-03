class Solution:
    def kthCharacter(self, k: int) -> str:
        result = 0
        while k != 1:                      #Iterate while k is not 1.
            t = k.bit_length() - 1         #Get the bit length of k then minus 1.
            if (1 << t) == k:              #Shift 1 left t times to get the bit mask of 2 ** k so that k == 2 ** t + a.
                t -= 1                     #If a == 0, reduce t by 1. Because if a == 0, current k-th number is the (2 ** t)-th character with 1 operation. Otherwise, current k-th number is the a-th character with 1 operation.
            k -= 1 << t                    #Deduct 2 ** t from k.
            result += 1                    #Increase result.
        return chr(ord("a") + result)      #Make result operations from 'a' and return.
