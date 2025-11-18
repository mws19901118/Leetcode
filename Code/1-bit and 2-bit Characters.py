class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if bits[-1]:                                                #If last digit is 1, it is definitely a 2-bit character.
            return False
        count = 0                                                   #Count the number of consecutive 1's in front of last digit.
        i = len(bits) - 2
        while i >= 0 and bits[i]:
            count += 1
            i -= 1
        return not count & 1                                        #Only when there are even length 1s, the last digit must be represented as the 1-bit character.
