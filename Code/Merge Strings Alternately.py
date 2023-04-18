class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i, j = 0, 0                                                                 #Initialize pointers i and j in word1 and word2 respectively.
        while i < len(word1) and j < len(word2):                                    #Traverse while i and j are both valid.
            result.append(word1[i] + word2[j])                                      #Append word1[i] and word2[j] to result.
            i += 1                                                                  #Move forward i.
            j += 1                                                                  #Move forward j.
        result.append((word1[i:] if i < len(word1) else word2[j:]))                 #Append the remaining of either word1 or word2 to result.
        return "".join(result)                                                      #Join result and return.
