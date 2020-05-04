class Solution:
    def findComplement(self, num: int) -> int:
        b = bin(num)[2:]                  #Convert num to binary.
        complement = 0
        for x in b:
            complement <<= 1              #Shift left complement.
            complement += (1 - int(x))    #Add the complement of each bit to complement.
        return complement
