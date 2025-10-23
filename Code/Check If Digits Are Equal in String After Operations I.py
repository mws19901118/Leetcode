class Solution:
    def hasSameDigits(self, s: str) -> bool:
        digits = [int(x) for x in s]                                    #Convert s to a list of digits.
        while len(digits) > 2:                                          #Iterate until there are only 2 digits.
            newDigits = []                                              #Initialize new digits.
            for i in range(len(digits) - 1):                            #Apply operations.
                newDigits.append((digits[i] + digits[i + 1]) % 10)
            digits = newDigits                                          #Replace digits with new digits.
        return digits[0] == digits[1]                                   #Return if the final 2 digits are equal.
