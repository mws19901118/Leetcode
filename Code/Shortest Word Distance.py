class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        i = 0
        while words[i] != word1 and words[i] != word2:            #Find the first occurrence of either word1 or word2.
            i += 1
        if words[i] == word1:                                     #If flag is true, it indicates that the last occurrence is word1.
            flag = True
        elif words[i] == word2:                                   #If flag is false, it indicates that the last occurrence is word2.
            flag = False
        result = len(words)
        last = i                                                  #Record the index of last occurrence of either word1 or word2.
        while i < len(words):
            if words[i] == word1:
                if flag is False:                                 #If current word is word1 and last occurrence is word2, update result and set flag to be false.
                    result = min(result, i - last)
                    flag = True
                last = i                                          #Update last occurrence.
            elif words[i] == word2:
                if flag is True:                                  #If current word is word2 and last occurrence is word1, update result and set flag to be true.
                    result = min(result, i - last)
                    flag = False
                last = i                                          #Update last occurrence.
            i += 1
        return result
