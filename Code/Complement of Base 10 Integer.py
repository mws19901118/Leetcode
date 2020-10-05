class Solution:
    def bitwiseComplement(self, N: int) -> int:
        binary = "{0:b}".format(N)        #Convert N to binary string.
        c = 0
        for b in binary:                  #Construct complement number using binary operation.
            c <<= 1
            c += 1 ^ int(b)
        return c
