class Solution:
    def concatenatedBinary(self, n: int) -> int:
        length = 1                                                  #Record current length of binary.
        exponentOf2 = 1                                             #Record the largest exponent of 2 which is not greater than current binary
        result = 0
        division = 10 ** 9 + 7                                      #Division is 10 ** 9 + 7.
        for i in range(1, n + 1):                                   #Traverse from 1 to n.
            if i == exponentOf2 << 1:                               #If i reaches a new exponent of 2, update exponentOf2 and length.
                exponentOf2 <<= 1
                length += 1
            result = ((result << length) + i) % division            #Shift result to left for length bit and add i then calculate the modulo.
        return result
