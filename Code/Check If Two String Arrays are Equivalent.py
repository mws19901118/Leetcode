class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        x1, y1, x2, y2 = 0, 0, 0, 0
        while x1 < len(word1) and x2 < len(word2) and word1[x1][y1] == word2[x2][y2]:       #Traverse word1 and word2 simultaneously and make sure the corresponding letters are the same.
            y1 += 1
            if y1 == len(word1[x1]):                                                        #If reaches the end of current word in word1, move to next word.
                x1 += 1
                y1 = 0
            y2 += 1
            if y2 == len(word2[x2]):                                                        #If reaches the end of current word in word2, move to next word.
                x2 += 1
                y2 = 0
        return x1 == len(word1) and x2 == len(word2)                                        #Check if both word1 and word2 are completely traversed.
