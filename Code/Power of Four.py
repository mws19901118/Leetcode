class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        binary = format(num, 'b')                                                                                   #Convert to binary.
        return len(binary) % 2 == 1 and binary[0] == '1' and all(x == '0' for x in binary[1:])                      #Check the length of binary is odd and most signification bit is 1 and the rest of binary is all 0.
