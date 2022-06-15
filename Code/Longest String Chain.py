class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        wordByLength = defaultdict(list)                                                                            #Group words by length.
        indexes = {}                                                                                                #Store the index of each word.
        for i, w in enumerate(words):                                                                               #Traverse words to populate wordByLength and indexes.
            wordByLength[len(w)].append(w)
            indexes[w] = i
        
        chainLength = [1] * len(words)                                                                              #Initialize the max length of chain starting at each index.
        for i in reversed(sorted(wordByLength.keys())):                                                             #Traverse words by length in descending order.
            for x in wordByLength[i]:
                for j in range(i):                                                                                  #Try remove each letter in x to get a new word y.
                    y = x[:j] + x[j + 1:]
                    if y in indexes:                                                                                #If y is a known word, there is a chain from y to x, so update chainLength[indexes[y]].
                        chainLength[indexes[y]] = max(chainLength[indexes[y]], chainLength[indexes[x]] + 1)
        return max(chainLength)                                                                                     #Return max length in chainLength.
