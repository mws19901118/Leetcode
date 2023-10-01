class Trie:

    def __init__(self):
        self.equalsToCount = 0                                                                                              #Store the count of current word.
        self.startsWithCount = 0                                                                                            #Store the count of words has current word as prefix.
        self.dictionary = defaultdict(lambda: Trie())                                                                       #Store next level trie nodes in defaultdict by letter.

    def insert(self, word: str) -> None:
        self.startsWithCount += 1                                                                                           #Increase startsWithCount.
        if not word:                                                                                                        #If this is the end of word, increase equalsToCount.
            self.equalsToCount += 1
        else:                                                                                                               #Otherwise, keep inserting to self.dictionary[word[0]] recursively.
            self.dictionary[word[0]].insert(word[1:])

    def countWordsEqualTo(self, word: str) -> int:
        return self.equalsToCount if not word else self.dictionary[word[0]].countWordsEqualTo(word[1:])                     #Return equalsToCount if it's the end of word; otherwise return the result from self.dictionary[word[0]].

    def countWordsStartingWith(self, prefix: str) -> int:
        return self.startsWithCount if not prefix else self.dictionary[prefix[0]].countWordsStartingWith(prefix[1:])        #Return startsWithCount if it's the end of prefix; otherwise return the result from self.dictionary[word[0]].


    def erase(self, word: str) -> None:
        self.startsWithCount -= 1                                                                                           #Decrease startsWithCount.
        if not word:                                                                                                        #If this is the end of word, increase equalsToCount.
            self.equalsToCount -= 1
        else:                                                                                                               #Otherwise, keep erasing from self.dictionary[word[0]] recursively.
            self.dictionary[word[0]].erase(word[1:])


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)
