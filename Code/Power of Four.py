class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        binary = "{0:b}".format(num)                                                                                #Convert to binary.
        return len(binary) % 2 == 1 and binary[0] == '1' and (binary[1:] == '' or int(binary[1:], 2) == 0)          #Check the length of binary is odd and most signification bit is 1 and the rest of binary is either empty or all 0.
