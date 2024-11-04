class Solution:
    def compressedString(self, word: str) -> str:
        i = 0
        result = ""
        while i < len(word):                                              #Traverse word.
            j = i
            while j < len(word) and j < i + 9 and word[i] == word[j]:     #While j is not the end and not greater than i + 9 and word[j] is same as word[i], move forward j.
                j += 1
            result += str(j - i) + word[i]                                #Compress word[i:j]
            i = j                                                         #Move i to j.
        return result
