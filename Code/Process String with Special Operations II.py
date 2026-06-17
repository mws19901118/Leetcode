class Solution:
    def processStr(self, s: str, k: int) -> str:
        length = 0                            #Initialize length.
        for x in s:                           #Traverse s.
            if x == "*":                      #If x == '*', decrease length by 1 if it is not zero.
                if length:
                    length -= 1
            elif x == '#':                    #If x == '*', double length.
                length *= 2
            elif x == '%':                    #If x == '%', continue as the length doesn't change.
                continue
            else:                             #Otherwise, increase length by 1.
                length += 1
        if k >= length:                       #If k >= length, k is out of bound, so return '.'.
            return '.'
        last = ''                             #Initialize the last character.
        for x in reversed(s):                 #Traverse s backwards.
            if k >= length:                   #If k >= length, we have found the k-th character, so stop.
                break
            if x == '*':                      #If x == '*', increase length by 1.
                length += 1
            elif x == '#':                    #If x == '#', reduce length by half and re-calculate k in new length.
                length //= 2
                k %= length
            elif x == '%':                    #If x == '%', update k to the opposite side.
                k = length - 1 - k
            else:                             #Otherwise, update last and decrease length.
                last = x
                length -= 1
        return last                           #Return last.
