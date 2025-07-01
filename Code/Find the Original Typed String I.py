class Solution:
    def possibleStringCount(self, word: str) -> int:
        i, result = 0, 0
        while i < len(word):                                    #Traverse word.
            j = i
            while j < len(word) and word[i] == word[j]:         #Find the length of current consecutive characters.
                j += 1
            result += j - i - 1                                 #For each chunk of consecutive characters word[i:j], there are j - i - 1 additional string representations. 
            i = j
        return result + 1                                       #Add 1 representations that removes duplicate consecutive characters, then return.
