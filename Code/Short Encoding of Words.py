class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        wordLengths = sorted([(len(w), i) for i, w in enumerate(words)], reverse = True)        #Sort index of each word according to word length in desending order.
        length = 0
        trie = {}                                                                               #Implement a trie using dictionary.
        for wordLength, wordIndex in wordLengths:                                               #Traverse words from the longest to shortest.
            word = words[wordIndex]
            level = trie                                                                        #Start from the root of trie.
            shouldAddToEncode = False                                                           #Indicate if current word should be add to encode referencing string explicitly.
            for i in range(wordLength - 1, -1, -1):                                             #Traverse word from behind.
                if word[i] not in level:                                                        #If current character not in current level of trie, current word is not included in any other word, so current word should be added to encode referencing string explicitly.
                    level[word[i]] = {}                                                         #Update trie.
                    shouldAddToEncode = True
                level = level[word[i]]                                                          #Move to next level of trie.
            if shouldAddToEncode:                                                               #Update encode referencing string length after adding current word, including the '#' after the word.
                length += wordLength + 1
        return length                                                                           #Return length.
