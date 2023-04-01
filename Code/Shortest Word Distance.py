class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        word1Prev, word2Prev = -1, -1                               #Store the previous index of word1 and word2 repectively, initially both -1.
        result = len(wordsDict)
        for i, x in enumerate(wordsDict):                           #Traverse wordsDict.
            if x == word1:                                          #Process when x is word1.
                if word2Prev >= 0:                                  #Update result if we have seen word2.
                    result = min(result, i - word2Prev)
                word1Prev = i                                       #Update word1Prev.
            elif x == word2:                                        #Process when x is word2.
                if word1Prev >= 0:                                  #Update result if we have seen word1.
                    result = min(result, i - word1Prev)
                word2Prev = i                                       #Update word2Prev.
        return result
