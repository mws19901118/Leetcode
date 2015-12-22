class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1 != word2:                                          #If words1 is not equal to words2, it's the same as Shortest Word Distance I.
            i = 0
            while words[i] != word1 and words[i] != word2:
                i += 1
            if words[i] == word1:
                flag = True
            elif words[i] == word2:
                flag = False
            result = len(words)
            last = i
            while i < len(words):
                if words[i] == word1:
                    if flag is False:
                        result = min(result, i - last)
                        flag = True
                    last = i
                elif words[i] == word2:
                    if flag is True:
                        result = min(result, i - last)
                        flag = False
                    last = i
                i += 1
            return result
        else:                                                       #Otherwise, find the shortest distance by checking every index of word1.
            result = len(words)
            last = words.index(word1)
            for i in range(last + 1, len(words)):
                if words[i] == word1:
                    result = min(result, i - last)
                    last = i
            return result
