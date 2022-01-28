class WordDictionary:

    def __init__(self):                                                                         #Initialize trie node.
        self.letters = {}
        self.hasWord = False

    def addWord(self, word: str) -> None:                                                       #Add word to trie.
        if not word:
            self.hasWord = True
            return
        if word[0] not in self.letters:
            self.letters[word[0]] = WordDictionary()
        self.letters[word[0]].addWord(word[1:])

    def search(self, word: str) -> bool:                                                        #Search word in trie.
        if not word:
            return self.hasWord
        if word[0] != '.':
            return word[0] in self.letters and self.letters[word[0]].search(word[1:])
        else:
            return any(self.letters[x].search(word[1:]) for x in self.letters)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
