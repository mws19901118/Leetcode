class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        wordToPattern, patternToWord = {}, {}                                                                                   #Store the mapping from word to pattern and mapping from pattern to word.
        words = s.split(' ')                                                                                                    #Split s by space to get words.
        if len(words) != len(pattern):                                                                                          #If length of words does not match the length of pattern, return false.
            return False
        for w, p in zip(words, pattern):                                                                                        #Traverse words and patterns.
            if w not in wordToPattern and p not in patternToWord:                                                               #If both word and pattern are not seen before, add mappings between each other.
                wordToPattern[w] = p
                patternToWord[p] = w
            elif w in wordToPattern and p in patternToWord and wordToPattern[w] == p and patternToWord[p] == w:                 #If both word and pattern are seen before, add they are mapped to each other, continue.
                continue
            else:                                                                                                               #Otherwise, return false.
                return False
        return True                                                                                                             #Return true.
