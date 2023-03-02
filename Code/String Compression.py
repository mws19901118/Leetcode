class Solution:
    def compress(self, chars: List[str]) -> int:
        index, i = 0, 0                                           #Intialize index of compressed string.
        while i < len(chars):                                     #Traver chars with 2 pointers.
            j = i
            while j < len(chars) and chars[j] == chars[i]:
                j += 1
            chars[index] = chars[i]                               #Set char[index] to current character.
            index += 1                                            #Increase index.
            if j - i > 1:                                         #If length of current charcter is greater than 0, covert length to string and append each character to compressed string.
                for x in str(j - i):
                    chars[index] = x
                    index += 1
            i = j
        return index                                              #Return index.
