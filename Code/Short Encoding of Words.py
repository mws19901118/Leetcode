class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        sortedWords = sorted(words, key = lambda w: len(w), reverse = True)                     #Sort words by word length in descending order.
        trie = {}                                                                               #Implement a trie using dictionary.
        count = 0
        for w in sortedWords:                                                                   #Traverse sorted word.
            shouldAdd = False                                                                   #Indicate if current word should be add to encode referencing string explicitly.
            node = trie                                                                         #Start from the root of trie.
            for x in reversed(w):                                                               #Traverse word from behind.
                if x not in node:                                                               #If current character not in current level of trie, current word is not included in any other word, so current word should be added to encode referencing string explicitly.
                    node[x] = {}                                                                #Update trie.
                    shouldAdd = True
                node = node[x]                                                                  #Move to next node of trie.
            if shouldAdd:                                                                       #Update encode referencing string length after adding current word, including the '#' after the word.
                count += len(w) + 1
        return count                                                                            #Return count.
