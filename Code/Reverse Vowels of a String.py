class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'                               #Initialize vowels.
        c = [x for x in s]                                  #Split s.
        i, j = 0, len(s) - 1                                #Initialize 2 pointers from start and end.
        while i < j:                                        #Traverse while i < j.
            while i < j and c[i] not in vowels:             #Move i to next vowel.
                i += 1
            while i < j and c[j] not in vowels:             #Move j to previous vowel.
                j -= 1
            if i < j:                                       #If still i < j, swap c[i] and c[j], increse i and decrease j.
                c[i], c[j] = c[j], c[i]
                i += 1
                j -= 1
        return "".join(c)                                   #Join c and return.
