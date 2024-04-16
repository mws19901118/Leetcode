class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0                                            #Initialize 2 pointers in word and abbr respectively.
        while i < len(word) and j < len(abbr):                 #Traverse while 2 pointers are valid.
            if abbr[j].isalpha():                              #If abbr[j] is letter, it has to be equal to word[i].
                if word[i] != abbr[j]:                         #If not, break.
                    break
                i += 1                                         #Otherwise, move forward i and j and continue.
                j += 1
                continue
            if abbr[j] == '0':                                 #Now abbr[j] is digit, since valid abbreviation cannot have leading 0, so break if abbr[j] is '0'.
                break
            k = j                                              #Find the whole number starting at abbr[j].
            while k < len(abbr) and abbr[k].isdigit():
                k += 1
            length = int(abbr[j:k])                            #Convert it to int.
            i += length                                        #Move i length characters forward.
            j = k                                              #Set j to k.
        return i == len(word) and j == len(abbr)               #Return if i and j are both exactly at the end of word and abbr.
