class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        if word1 == word2:                                                      #If word1 and word2 are same, find the shortest distance by checking every index of word1.
            prev = -1
            result = len(wordsDict)
            for i, x in enumerate(wordsDict):
                if x == word1:
                    if prev >= 0:
                        result = min(result, i - prev)
                    prev = i
            return result
        word1Prev, word2Prev = -1, -1                                           #Otherwise, it's the same as Shortest Word Distance I.
        result = len(wordsDict)
        for i, x in enumerate(wordsDict):
            if x == word1:
                if word2Prev >= 0:
                    result = min(result, i - word2Prev)
                word1Prev = i
            elif x == word2:
                if word1Prev >= 0:
                    result = min(result, i - word1Prev)
                word2Prev = i
        return result
