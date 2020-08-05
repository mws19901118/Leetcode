class WordDictionary:

    def __init__(self):                                                                                                             #Essentially, it's a Trie.
        """
        Initialize your data structure here.
        """
        self.letters = {}
        self.hasWord = False
        
    def addWord(self, word: str) -> None:                                                                                           #Add word to Trie.
        """
        Adds a word into the data structure.
        """
        if word == "":
            self.hasWord = True
            return
        if word[0] not in self.letters:
            self.letters[word[0]] = WordDictionary()
        self.letters[word[0]].addWord(word[1:])

    def search(self, word: str) -> bool:                                                                                            #Search word in Trie.
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if word == "":
            return self.hasWord
        if word[0] != '.':
            if word[0] not in self.letters:
                return False
            return self.letters[word[0]].search(word[1:])
        else:                                                                                                                       #If the first letter is '.', traverse all its children.
            return any(self.letters[x].search(word[1:]) for x in self.letters)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
